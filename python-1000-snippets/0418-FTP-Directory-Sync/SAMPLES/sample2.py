# sample2.py
# Demonstrates uploading a file to an FTP server using a minimal FTP client implementation.

import os
import socket
import threading
import tempfile
import time

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def _start_ftp_server(root_dir: str) -> tuple[FTPServer, int]:
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "12345", root_dir, perm="elradfmwMT")

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("127.0.0.1", 0), handler)
    port = server.socket.getsockname()[1]

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, port


def _recv_line(f) -> str:
    return f.readline().decode("utf-8").rstrip("\r\n")


def _send_cmd(f, cmd: str) -> str:
    f.write((cmd + "\r\n").encode("utf-8"))
    f.flush()
    return _recv_line(f)


def _parse_pasv(resp: str) -> tuple[str, int]:
    start = resp.find("(")
    end = resp.find(")", start)
    if start < 0 or end < 0:
        raise ValueError("Invalid PASV response: %r" % resp)
    numbers = resp[start + 1 : end].split(",")
    host = ".".join(numbers[:4])
    port = int(numbers[4]) * 256 + int(numbers[5])
    return host, port


def main() -> None:
    with tempfile.TemporaryDirectory() as server_root, tempfile.TemporaryDirectory() as client_root:
        local_file = os.path.join(client_root, "upload.txt")
        with open(local_file, "w", encoding="utf-8") as f:
            f.write("Uploaded from client\n")

        server, port = _start_ftp_server(server_root)
        time.sleep(0.2)

        try:
            with socket.create_connection(("127.0.0.1", port), timeout=5) as sock:
                f = sock.makefile("rwb")
                print(_recv_line(f))
                print(_send_cmd(f, "USER user"))
                print(_send_cmd(f, "PASS 12345"))
                print(_send_cmd(f, "TYPE I"))

                pasv_resp = _send_cmd(f, "PASV")
                host, data_port = _parse_pasv(pasv_resp)

                # Upload file via data connection.
                with socket.create_connection((host, data_port), timeout=5) as data_sock:
                    print(_send_cmd(f, "STOR upload.txt"))
                    with open(local_file, "rb") as file_obj:
                        data_sock.sendall(file_obj.read())

                print(_recv_line(f))  # transfer complete
                print(_send_cmd(f, "QUIT"))

            # Verify the file ended up on the server.
            server_file = os.path.join(server_root, "upload.txt")
            with open(server_file, "r", encoding="utf-8") as f:
                print("Server has file content:", f.read().strip())
        finally:
            server.close_all()


if __name__ == "__main__":
    main()
