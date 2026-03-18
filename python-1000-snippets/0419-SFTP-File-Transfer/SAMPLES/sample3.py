# sample3.py
# Demonstrates syncing directories between a local filesystem and an SFTP server using asyncssh.

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
        # Prepare a small directory tree on the server.
        remote_dir = os.path.join(root_dir, "remote_dir")
        os.makedirs(remote_dir, exist_ok=True)
        server_file = os.path.join(remote_dir, "remote.txt")
        with open(server_file, "w", encoding="utf-8") as f:
            f.write("Hello from remote directory\n")

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
                # Download the remote directory into a local directory.
                local_sync_dir = os.path.join(local_dir, "sync")
                os.makedirs(local_sync_dir, exist_ok=True)

                await sftp.get("remote_dir", local_sync_dir, recurse=True)
                print("Downloaded remote_dir into", local_sync_dir)

                # Create a local directory to upload.
                local_upload_dir = os.path.join(local_dir, "upload")
                os.makedirs(local_upload_dir, exist_ok=True)
                upload_file = os.path.join(local_upload_dir, "new.txt")
                with open(upload_file, "w", encoding="utf-8") as f:
                    f.write("Hello from local upload\n")

                # Upload the directory into the server's root.
                await sftp.put(local_upload_dir, "uploaded", recurse=True)

                print("Server root listing:", await sftp.listdir("."))
                print("Server uploaded directory listing:", await sftp.listdir("uploaded"))

                async with sftp.open("uploaded/new.txt", "r") as f:
                    print("Uploaded file content:", (await f.read()).strip())

        server.close()
        await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
