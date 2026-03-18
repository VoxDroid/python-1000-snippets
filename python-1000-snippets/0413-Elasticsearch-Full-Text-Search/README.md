# Elasticsearch Full-Text Search

## Description
This snippet shows how to start a local Elasticsearch node (bundled with this repo), index sample documents, and run full-text searches using the Python `elasticsearch` client.

## Requirements
- Python 3.8+
- `elasticsearch` Python package (`pip install elasticsearch`)
- No external Elasticsearch server required—the snippet starts a local instance.

## Code
```python
"""Run this file to start a local Elasticsearch node and perform full-text searches."""

import os
import socket
import subprocess
import tempfile
import time

from elasticsearch import Elasticsearch


def _repo_root() -> str:
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..")
    )


def _ensure_temp_dir() -> str:
    root = _repo_root()
    temp_dir = os.path.join(root, "temp", "elasticsearch")
    os.makedirs(temp_dir, exist_ok=True)
    return temp_dir


def _find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _start_elasticsearch(port: int, temp_dir: str) -> subprocess.Popen:
    es_home = os.path.join(_repo_root(), "elasticsearch")

    data_dir = os.path.join(temp_dir, "data")
    logs_dir = os.path.join(temp_dir, "logs")
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)

    env = os.environ.copy()
    env["ES_JAVA_OPTS"] = "-Xms256m -Xmx512m"
    env["JAVA_HOME"] = os.path.join(es_home, "jdk")
    env["PATH"] = os.path.join(env["JAVA_HOME"], "bin") + ":" + env.get("PATH", "")

    es_bin = os.path.join(es_home, "bin", "elasticsearch")
    args = [
        es_bin,
        "-E", f"path.data={data_dir}",
        "-E", f"path.logs={logs_dir}",
        "-E", "discovery.type=single-node",
        "-E", f"http.port={port}",
        "-E", "network.host=127.0.0.1",
    ]

    return subprocess.Popen(
        args,
        stdout=open(os.path.join(logs_dir, "elasticsearch.log"), "a", encoding="utf-8"),
        stderr=subprocess.STDOUT,
        env=env,
        close_fds=True,
    )


def main() -> None:
    temp_dir = _ensure_temp_dir()
    port = _find_free_port()

    proc = _start_elasticsearch(port=port, temp_dir=temp_dir)

    # Wait for Elasticsearch to start.
    deadline = time.time() + 60
    es = None
    while time.time() < deadline:
        try:
            es = Elasticsearch([f"http://127.0.0.1:{port}"])
            if es.ping():
                break
        except Exception:
            time.sleep(0.5)

    if es is None or not es.ping():
        proc.terminate()
        raise RuntimeError("Elasticsearch failed to start")

    try:
        index = "documents"
        es.indices.create(index=index, ignore=400)

        docs = [
            {"id": 1, "content": "The quick brown fox jumps over the lazy dog."},
            {"id": 2, "content": "Python is a great language for text analysis."},
            {"id": 3, "content": "Elasticsearch provides full-text search capabilities."},
        ]

        for doc in docs:
            es.index(index=index, id=doc["id"], document=doc)

        es.indices.refresh(index=index)

        query = {"query": {"match": {"content": "text"}}}
        resp = es.search(index=index, query=query)

        print("Found hits:", resp["hits"]["total"]["value"])
        for hit in resp["hits"]["hits"]:
            print(hit["_source"])

    finally:
        proc.terminate()
        proc.wait(timeout=30)


if __name__ == "__main__":
    main()
```

## Output
A successful run will print something like:

```
Found hits: 2
{'id': 2, 'content': 'Python is a great language for text analysis.'}
{'id': 3, 'content': 'Elasticsearch provides full-text search capabilities.'}
```

## Notes
- The server runs locally on a dynamically chosen port and is shut down after the script completes.
- Logs and data are stored under `./temp/elasticsearch/`.
