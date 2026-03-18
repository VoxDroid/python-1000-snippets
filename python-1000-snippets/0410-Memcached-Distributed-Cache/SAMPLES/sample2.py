# sample2.py
# Demonstrates expiry (TTL) behavior in Memcached using pymemcache.

import os
import socket
import subprocess
import tempfile
import time

from pymemcache.client.base import Client


def _repo_root() -> str:
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..")
    )


def _ensure_temp_dir() -> str:
    root = _repo_root()
    temp_dir = os.path.join(root, "temp")
    os.makedirs(temp_dir, exist_ok=True)
    return temp_dir


def _find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def _start_memcached(port: int, log_path: str) -> subprocess.Popen:
    return subprocess.Popen(
        [
            "memcached",
            "-p",
            str(port),
            "-l",
            "127.0.0.1",
            "-U",
            "0",
        ],
        stdout=open(log_path, "a", encoding="utf-8"),
        stderr=subprocess.STDOUT,
        close_fds=True,
    )


def main() -> None:
    temp_dir = _ensure_temp_dir()
    log_path = os.path.join(temp_dir, "memcached.log")

    port = _find_free_port()
    proc = _start_memcached(port=port, log_path=log_path)

    # Wait until memcached is ready.
    deadline = time.time() + 5
    while time.time() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.3):
                break
        except OSError:
            time.sleep(0.05)
    else:
        proc.terminate()
        raise RuntimeError("memcached failed to start")

    try:
        client = Client(("127.0.0.1", port), connect_timeout=1, timeout=1)

        # Set a key that expires after 2 seconds.
        client.set("expiring", "gone", expire=2)
        print("before expiry:", client.get("expiring"))

        time.sleep(3)
        print("after expiry:", client.get("expiring"))

    finally:
        proc.terminate()
        proc.wait(timeout=5)


if __name__ == "__main__":
    main()
