# sample2.py
# Demonstrates capturing stdout/stderr and return codes from remote SSH commands.

import asyncio
import socket

import asyncssh


class MySSHServerSession(asyncssh.SSHServerSession):
    def __init__(self):
        self._chan = None
        self._command = None

    def connection_made(self, chan):
        self._chan = chan

    def exec_requested(self, command: str) -> bool:
        self._command = command
        return True

    def session_started(self):
        asyncio.create_task(self._run_command())

    async def _run_command(self):
        if self._command is None:
            return

        proc = await asyncio.create_subprocess_shell(
            self._command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()

        if stdout:
            self._chan.write(stdout.decode())
        if stderr:
            self._chan.write_stderr(stderr.decode())

        self._chan.exit(proc.returncode)
        self._chan.close()


class MySSHServer(asyncssh.SSHServer):
    def begin_auth(self, username):
        return True

    def password_auth_supported(self):
        return True

    def validate_password(self, username, password):
        return username == "user" and password == "12345"

    def session_requested(self):
        return MySSHServerSession()


async def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]

    host_key = asyncssh.generate_private_key("ssh-rsa")

    server = await asyncssh.create_server(
        MySSHServer,
        "127.0.0.1",
        port,
        server_host_keys=[host_key],
        password_auth=True,
    )

    try:
        print("SSH server listening on port", port)

        async with asyncssh.connect(
            "127.0.0.1",
            port=port,
            username="user",
            password="12345",
            known_hosts=None,
        ) as conn:
            # Run a command that will exit with a non-zero code.
            result = await conn.run("ls /nonexistent", check=False)
            print("Return code:", result.exit_status)
            print("Stderr:", result.stderr.strip())
    finally:
        server.close()
        await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
