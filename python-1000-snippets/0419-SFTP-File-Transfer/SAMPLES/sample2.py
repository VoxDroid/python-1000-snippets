# sample2.py
# Demonstrates uploading a file to an SFTP server using asyncssh.

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
    with tempfile.TemporaryDirectory() as root_dir, tempfile.TemporaryDirectory() as local_dir:
        # Create an existing file on the server side.
        server_file = os.path.join(root_dir, "hello.txt")
        with open(server_file, "w", encoding="utf-8") as f:
            f.write("Hello from SFTP server\n")

        # Create a local file we will upload.
        upload_file = os.path.join(local_dir, "upload.txt")
        with open(upload_file, "w", encoding="utf-8") as f:
            f.write("Hello from the local client\n")

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
                # Upload the local file into the server root.
                await sftp.put(upload_file, "upload.txt")

                # List files on the server and read back the uploaded content.
                print("Remote files:", await sftp.listdir("."))
                async with sftp.open("upload.txt", "r") as f:
                    content = await f.read()
                    print("Uploaded content:", content.strip())

        server.close()
        await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
