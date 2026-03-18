# sample2.py
# Demonstrates using $project and $sort stages in an aggregation pipeline.

import os
import socket
import subprocess
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
        coll = db["products"]
        coll.delete_many({})

        coll.insert_many(
            [
                {"name": "apple", "price": 1.2, "stock": 10},
                {"name": "orange", "price": 0.9, "stock": 5},
                {"name": "banana", "price": 0.5, "stock": 0},
            ]
        )

        pipeline = [
            {"$match": {"stock": {"$gt": 0}}},
            {"$project": {"_id": 0, "name": 1, "inventoryValue": {"$multiply": ["$price", "$stock"]}}},
            {"$sort": {"inventoryValue": -1}},
        ]

        print("Projected inventory values:")
        for doc in coll.aggregate(pipeline):
            print(doc)

    finally:
        proc.terminate()
        proc.wait(timeout=5)


if __name__ == "__main__":
    main()
