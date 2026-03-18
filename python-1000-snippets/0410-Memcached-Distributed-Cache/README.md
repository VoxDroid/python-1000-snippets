# Memcached Distributed Cache

## Description
This snippet demonstrates using Memcached as an in-memory distributed cache.
It starts a local `memcached` server (from the system binary), performs cache operations with `pymemcache`, and shuts down the server cleanly.

## Requirements
- Python 3.8+
- System `memcached` binary available in `PATH` (e.g., `sudo apt install memcached`)
- Python dependency: `pymemcache` (`pip install pymemcache`)

## Code
```python
"""Run this file to exercise Memcached cache operations."""

import os
import socket
import subprocess
import sys
import tempfile
import time

from pymemcache.client.base import Client


def _repo_root() -> str:
    # Assumes this file is in `.../python-1000-snippets/<snippet>/SAMPLES/`.
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..")
    )


def _ensure_temp_dir() -> str:
    root = _repo_root()
    temp_dir = os.path.join(root, "temp")
    os.makedirs(temp_dir, exist_ok=True)
    return temp_dir


def _find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


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

    # Wait until the server is accepting connections.
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

        print("Set key=mykey")
        client.set("mykey", "value")

        print("Get key=mykey ->", client.get("mykey"))

        print("Increment counter")
        client.set("counter", 0)
        client.incr("counter", 1)
        client.incr("counter", 2)
        print("counter ->", client.get("counter"))

        print("Fetch multiple keys")
        print(client.get_many(["mykey", "counter"]))

    finally:
        proc.terminate()
        proc.wait(timeout=5)


if __name__ == "__main__":
    main()
```

## Output
Running the script should print output similar to:

```
Set key=mykey
Get key=mykey -> b'value'
Increment counter
counter -> b'3'
Fetch multiple keys
{b'mykey': b'value', b'counter': b'3'}
```

## Notes
- This snippet uses a local `memcached` process so the examples can run without requiring an externally managed cache server.
- Logs for the memcached process are written to `./temp/memcached.log`.
