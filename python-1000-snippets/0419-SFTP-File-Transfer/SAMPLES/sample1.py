# sample1.py
# Demonstrates an SFTP server and client using asyncssh.

import asyncio
import os
import tempfile

import asyncssh


class MySSHServer(asyncssh.SSHServer):
    def begin_auth(self, username):
        return True

    def password_auth_supported(self):
        return True

    def validate_password(self, username, password):
        return username == "user" and password == "12345"


async def main() -> None:
    with tempfile.TemporaryDirectory() as root_dir:
        # Create a file on the server side.
        path = os.path.join(root_dir, "hello.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write("Hello from SFTP server\n")

        host_key = asyncssh.generate_private_key("ssh-rsa")

        def sftp_factory(chan):
            return asyncssh.SFTPServer(chan, chroot=root_dir.encode("utf-8"))

        server = await asyncssh.create_server(
            MySSHServer,
            "127.0.0.1",
            0,
            server_host_keys=[host_key],
            sftp_factory=sftp_factory,
            password_auth=True,
        )

        port = server.get_port()
        print("SFTP server listening on port", port)

        async with asyncssh.connect(
            "127.0.0.1",
            port=port,
            username="user",
            password="12345",
            known_hosts=None,
        ) as conn:
            async with conn.start_sftp_client() as sftp:
                print("Remote files:", await sftp.listdir("."))
                async with sftp.open("hello.txt", "r") as f:
                    content = await f.read()
                    print("Downloaded content:", content.strip())

        server.close()
        await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
