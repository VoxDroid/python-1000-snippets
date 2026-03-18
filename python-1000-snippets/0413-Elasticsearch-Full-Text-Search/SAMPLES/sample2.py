# sample2.py
# Demonstrates using analyzers and multi-match queries.

import os
import shutil
import socket
import subprocess
import time

from elasticsearch import Elasticsearch


def _repo_root() -> str:
    # Use an absolute file path in case the script is executed via a relative path.
    script_path = os.path.abspath(__file__)
    return os.path.abspath(
        os.path.join(os.path.dirname(script_path), "..", "..", "..")
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

    # Do a clean start for reproducibility (avoids stale state/config issues).
    shutil.rmtree(data_dir, ignore_errors=True)
    shutil.rmtree(logs_dir, ignore_errors=True)
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
        "-E", "xpack.security.enabled=false",
        "-E", "xpack.security.enrollment.enabled=false",
        "-E", "xpack.security.http.ssl.enabled=false",
        "-E", "xpack.security.transport.ssl.enabled=false",
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

    # Wait for Elasticsearch to be available.
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
        index = "articles"
        settings = {
            "settings": {
                "analysis": {
                    "analyzer": {
                        "custom_english": {
                            "type": "custom",
                            "tokenizer": "standard",
                            "filter": ["lowercase", "stop", "porter_stem"],
                        }
                    }
                }
            }
        }
        es.indices.create(index=index, body=settings, ignore=400)

        docs = [
            {"id": 1, "title": "Python tips", "content": "Use list comprehensions for concise loops."},
            {"id": 2, "title": "Elasticsearch guide", "content": "Full-text search uses inverted indices."},
            {"id": 3, "title": "Data modeling", "content": "Design indexes for the queries you need."},
        ]

        for doc in docs:
            es.index(index=index, id=doc["id"], document=doc)

        es.indices.refresh(index=index)

        query = {"multi_match": {"query": "search", "fields": ["title", "content"]}}
        resp = es.search(index=index, query=query)

        print("Found hits:", resp["hits"]["total"]["value"])
        for hit in resp["hits"]["hits"]:
            print(hit["_source"])

    finally:
        proc.terminate()
        proc.wait(timeout=30)


if __name__ == "__main__":
    main()
