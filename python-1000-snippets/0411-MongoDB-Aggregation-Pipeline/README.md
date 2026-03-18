# MongoDB Aggregation Pipeline

## Description
This snippet demonstrates using MongoDB aggregation pipelines to process and analyze data.
It starts a local MongoDB server from the bundled `mongod` binary, inserts sample documents, and runs multiple aggregation pipelines.

## Requirements
- Python 3.8+
- `pymongo` (`pip install pymongo`)
- MongoDB server binary provided under `mongodb-linux/.../bin/mongod` (bundled in this repo)

## Code
```python
"""Run this file to start a local MongoDB server and execute aggregation pipelines."""

import os
import socket
import subprocess
import tempfile
import time

from pymongo import MongoClient


def _repo_root() -> str:
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..")
    )


def _ensure_temp_dir() -> str:
    root = _repo_root()
    temp_dir = os.path.join(root, "temp")
    os.makedirs(temp_dir, exist_ok=True)
    return temp_dir


def _mongod_binary() -> str:
    root = _repo_root()
    return os.path.join(
        root,
        "mongodb-linux",
        "mongodb-linux-x86_64-ubuntu2204-7.0.5",
        "bin",
        "mongod",
    )


def _find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def _start_mongod(port: int, dbpath: str, log_path: str) -> subprocess.Popen:
    return subprocess.Popen(
        [
            _mongod_binary(),
            "--dbpath",
            dbpath,
            "--bind_ip",
            "127.0.0.1",
            "--port",
            str(port),
            "--quiet",
        ],
        stdout=open(log_path, "a", encoding="utf-8"),
        stderr=subprocess.STDOUT,
        close_fds=True,
    )


def main() -> None:
    temp_dir = _ensure_temp_dir()

    port = _find_free_port()
    dbpath = os.path.join(temp_dir, "mongodb-data")
    os.makedirs(dbpath, exist_ok=True)

    log_path = os.path.join(temp_dir, "mongodb.log")
    proc = _start_mongod(port=port, dbpath=dbpath, log_path=log_path)

    # Wait for MongoDB to accept connections.
    deadline = time.time() + 10
    client = None
    while time.time() < deadline:
        try:
            client = MongoClient(f"mongodb://127.0.0.1:{port}/", serverSelectionTimeoutMS=1000)
            client.admin.command("ping")
            break
        except Exception:
            time.sleep(0.1)

    if client is None:
        proc.terminate()
        raise RuntimeError("mongod failed to start")

    try:
        db = client["sample_db"]
        coll = db["items"]
        coll.delete_many({})

        docs = [
            {"category": "fruit", "value": 10},
            {"category": "fruit", "value": 5},
            {"category": "vegetable", "value": 7},
            {"category": "vegetable", "value": 3},
        ]
        coll.insert_many(docs)

        pipeline = [
            {"$match": {"value": {"$gt": 0}}},
            {"$group": {"_id": "$category", "total": {"$sum": "$value"}}},
            {"$sort": {"total": -1}},
        ]

        print("Aggregation result:")
        for doc in coll.aggregate(pipeline):
            print(doc)

    finally:
        proc.terminate()
        proc.wait(timeout=5)


if __name__ == "__main__":
    main()
```

## Output
You should see aggregation results similar to:

```
Aggregation result:
{'_id': 'fruit', 'total': 15}
{'_id': 'vegetable', 'total': 10}
```

## Notes
- The script runs a standalone local MongoDB server, so no external MongoDB instance is required.
- Logs are written to `./temp/mongodb.log`.
