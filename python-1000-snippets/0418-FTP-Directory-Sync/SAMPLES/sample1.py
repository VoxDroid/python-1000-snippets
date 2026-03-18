# sample1.py
# Demonstrates syncing a file from an FTP server using a minimal FTP client.

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
    # Read a response line from the FTP control connection.
    return f.readline().decode("utf-8").rstrip("\r\n")


def _send_cmd(f, cmd: str) -> str:
    f.write((cmd + "\r\n").encode("utf-8"))
    f.flush()
    return _recv_line(f)


def _parse_pasv(resp: str) -> tuple[str, int]:
    # Example: 227 Entering Passive Mode (127,0,0,1,195,132).
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
        server_file = os.path.join(server_root, "hello.txt")
        with open(server_file, "w", encoding="utf-8") as f:
            f.write("Hello from FTP server\n")

        server, port = _start_ftp_server(server_root)

        # Wait a moment for the server accept loop to start.
        time.sleep(0.2)

        try:
            with socket.create_connection(("127.0.0.1", port), timeout=5) as sock:
                f = sock.makefile("rwb")
                print(_recv_line(f))  # banner
                print(_send_cmd(f, "USER user"))
                print(_send_cmd(f, "PASS 12345"))
                print(_send_cmd(f, "TYPE I"))

                # Enter passive mode and download the file.
                pasv_resp = _send_cmd(f, "PASV")
                host, data_port = _parse_pasv(pasv_resp)

                with socket.create_connection((host, data_port), timeout=5) as data_sock:
                    print(_send_cmd(f, "RETR hello.txt"))
                    data = data_sock.recv(1024)
                    print("Downloaded content:", data.decode("utf-8").strip())

                print(_recv_line(f))  # transfer complete
                print(_send_cmd(f, "QUIT"))
        finally:
            server.close_all()


if __name__ == "__main__":
    main()
