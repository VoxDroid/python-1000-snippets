# Cassandra Data Modeling

## Description
This snippet demonstrates Cassandra data modeling patterns by starting a local Cassandra instance (bundled in the repository), creating keyspaces and tables, and running CQL queries using the Python `cassandra-driver`.

## Requirements
- Python 3.8+
- `cassandra-driver` (`pip install cassandra-driver`)
- Java (required by Cassandra; typically available on Ubuntu)
- The Cassandra distribution included under `cassandra/` in this repo

## Code
```python
"""Run this file to start Cassandra locally and exercise basic data modeling patterns."""

import os
import shutil
import socket
import subprocess
import tempfile
import time

from cassandra.cluster import Cluster


def _repo_root() -> str:
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..")
    )


def _ensure_temp_dir() -> str:
    root = _repo_root()
    temp_dir = os.path.join(root, "temp", "cassandra")
    os.makedirs(temp_dir, exist_ok=True)
    return temp_dir


def _find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def _build_classpath(cassandra_home: str, cassandra_conf: str) -> str:
    jars = []
    jars.append(cassandra_conf)
    for jar in sorted(os.listdir(os.path.join(cassandra_home, "lib"))):
        if jar.endswith(".jar"):
            jars.append(os.path.join(cassandra_home, "lib", jar))
    # include JSR223 jar directories if present
    jsr223_dir = os.path.join(cassandra_home, "lib", "jsr223")
    if os.path.isdir(jsr223_dir):
        for root, _, files in os.walk(jsr223_dir):
            for f in files:
                if f.endswith(".jar"):
                    jars.append(os.path.join(root, f))
    return ":".join(jars)


def _write_config(temp_conf: str, port: int, data_dir: str) -> None:
    import yaml

    src_conf = os.path.join(_repo_root(), "cassandra", "conf")
    shutil.copytree(src_conf, temp_conf, dirs_exist_ok=True)

    config_path = os.path.join(temp_conf, "cassandra.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    config["listen_address"] = "127.0.0.1"
    config["rpc_address"] = "127.0.0.1"
    config["native_transport_port"] = port
    config["storage_port"] = _find_free_port()
    config["ssl_storage_port"] = _find_free_port()
    config["data_file_directories"] = [os.path.join(data_dir, "data")]
    config["commitlog_directory"] = os.path.join(data_dir, "commitlog")
    config["saved_caches_directory"] = os.path.join(data_dir, "saved_caches")
    config["hints_directory"] = os.path.join(data_dir, "hints")

    for key in ["data_file_directories", "commitlog_directory", "saved_caches_directory", "hints_directory"]:
        os.makedirs(config[key][0] if isinstance(config[key], list) else config[key], exist_ok=True)

    with open(config_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(config, f)


def _start_cassandra(port: int, temp_dir: str) -> subprocess.Popen:
    cassandra_home = os.path.join(_repo_root(), "cassandra")
    temp_conf = os.path.join(temp_dir, "conf")
    data_dir = os.path.join(temp_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    _write_config(temp_conf, port, data_dir)

    log_dir = os.path.join(temp_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)

    env = os.environ.copy()
    env["CASSANDRA_HOME"] = cassandra_home
    env["CASSANDRA_CONF"] = temp_conf
    env["CASSANDRA_LOG_DIR"] = log_dir
    env["CLASSPATH"] = _build_classpath(cassandra_home, temp_conf)

    cassandra_bin = os.path.join(cassandra_home, "bin", "cassandra")
    log_path = os.path.join(log_dir, "cassandra.log")

    return subprocess.Popen(
        [cassandra_bin, "-f"],
        stdout=open(log_path, "a", encoding="utf-8"),
        stderr=subprocess.STDOUT,
        env=env,
        close_fds=True,
    )


def main() -> None:
    temp_dir = _ensure_temp_dir()
    port = _find_free_port()

    proc = _start_cassandra(port=port, temp_dir=temp_dir)

    # Wait for Cassandra to accept connections.
    deadline = time.time() + 60
    cluster = None
    while time.time() < deadline:
        try:
            cluster = Cluster(["127.0.0.1"], port=port, connect_timeout=1)
            session = cluster.connect()
            session.execute("SELECT now() FROM system.local")
            break
        except Exception:
            time.sleep(1)

    if cluster is None:
        proc.terminate()
        raise RuntimeError("Cassandra failed to start")

    try:
        session = cluster.connect()
        session.execute("CREATE KEYSPACE IF NOT EXISTS testks WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}")
        session.set_keyspace("testks")
        session.execute(
            "CREATE TABLE IF NOT EXISTS users (id int PRIMARY KEY, name text, age int)"
        )
        session.execute("INSERT INTO users (id, name, age) VALUES (1, 'Alice', 30)")
        session.execute("INSERT INTO users (id, name, age) VALUES (2, 'Bob', 25)")

        rows = session.execute("SELECT id, name, age FROM users")
        for row in rows:
            print(row)

    finally:
        if cluster is not None:
            cluster.shutdown()
        proc.terminate()
        proc.wait(timeout=10)


if __name__ == "__main__":
    main()
```

## Output
The script prints the inserted rows, e.g.:

```
Row(id=1, name='Alice', age=30)
Row(id=2, name='Bob', age=25)
```

## Notes
- A local Cassandra instance is started for the snippet and shut down afterward.
- Configuration and data are stored under `./temp/cassandra/`.
