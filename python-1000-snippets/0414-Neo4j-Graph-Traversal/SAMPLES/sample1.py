# sample1.py
# Demonstrates creating and querying a node using a local Neo4j server.

import os
import shutil
import socket
import subprocess
import tarfile
import time

from neo4j import GraphDatabase


def _repo_root() -> str:
    # Support invocation via a relative path (e.g., `python SAMPLES/sample1.py`).
    script_path = os.path.abspath(__file__)
    return os.path.abspath(os.path.join(os.path.dirname(script_path), "..", "..", ".."))


def _ensure_temp_dir() -> str:
    root = _repo_root()
    temp_dir = os.path.join(root, "temp", "neo4j")
    os.makedirs(temp_dir, exist_ok=True)
    return temp_dir


def _find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _ensure_neo4j_distribution(neo4j_root: str) -> None:
    # Download/expand Neo4j if it is not already present.
    if os.path.isdir(os.path.join(neo4j_root, "bin")):
        return

    url = "https://dist.neo4j.org/neo4j-community-4.4.26-unix.tar.gz"
    archive = os.path.join(neo4j_root, "neo4j-community.tar.gz")
    print(f"Downloading Neo4j from {url} ...", flush=True)

    import urllib.request

    urllib.request.urlretrieve(url, archive)

    print("Extracting Neo4j distribution...", flush=True)
    with tarfile.open(archive, "r:gz") as tf:
        # Strip the top-level directory from the archive.
        members = []
        for member in tf.getmembers():
            parts = member.name.split("/", 1)
            if len(parts) > 1:
                member.name = parts[1]
                members.append(member)
        tf.extractall(path=neo4j_root, members=members)


def _start_neo4j(temp_dir: str, bolt_port: int, http_port: int) -> subprocess.Popen:
    root = _repo_root()
    neo4j_root = os.path.join(root, "temp", "neo4j")
    _ensure_neo4j_distribution(neo4j_root)

    # Ensure the configuration matches our test environment.
    conf_path = os.path.join(neo4j_root, "conf", "neo4j.conf")
    if os.path.exists(conf_path):
        with open(conf_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        def set_prop(key: str, value: str) -> None:
            prefix = key + "="
            for i, line in enumerate(lines):
                stripped = line.strip()
                if stripped.startswith(prefix) or stripped.startswith("#" + prefix):
                    lines[i] = f"{key}={value}\n"
                    return
            lines.append(f"{key}={value}\n")

        set_prop("dbms.security.auth_enabled", "false")
        set_prop("dbms.connector.bolt.listen_address", f"127.0.0.1:{bolt_port}")
        set_prop("dbms.connector.http.listen_address", f"127.0.0.1:{http_port}")
        set_prop("dbms.memory.heap.initial_size", "256m")
        set_prop("dbms.memory.heap.max_size", "512m")

        with open(conf_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

    data_dir = os.path.join(temp_dir, "data")
    logs_dir = os.path.join(temp_dir, "logs")
    shutil.rmtree(data_dir, ignore_errors=True)
    shutil.rmtree(logs_dir, ignore_errors=True)
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)

    env = os.environ.copy()
    # Neo4j 4.x requires Java 11
    env["JAVA_HOME"] = "/usr/lib/jvm/java-1.11.0-openjdk-amd64"
    env["NEO4J_ACCEPT_LICENSE_AGREEMENT"] = "yes"

    neo4j_bin = os.path.join(neo4j_root, "bin", "neo4j")

    log_path = os.path.join(logs_dir, "neo4j.log")
    return subprocess.Popen(
        [neo4j_bin, "console"],
        stdout=open(log_path, "a", encoding="utf-8"),
        stderr=subprocess.STDOUT,
        env=env,
        close_fds=True,
    )


def main() -> None:
    temp_dir = _ensure_temp_dir()
    bolt_port = 7687
    http_port = 7474

    proc = _start_neo4j(temp_dir=temp_dir, bolt_port=bolt_port, http_port=http_port)

    # Wait for Neo4j to accept Bolt connections.
    deadline = time.time() + 60
    driver = None
    last_exc = None
    while time.time() < deadline:
        try:
            # Pass an empty auth tuple; the server is configured to disable auth.
            driver = GraphDatabase.driver(
                f"bolt://127.0.0.1:{bolt_port}", auth=("", ""), encrypted=False
            )
            with driver.session() as session:
                session.run("RETURN 1").single()
            break
        except Exception as exc:
            last_exc = exc
            time.sleep(0.5)

    if driver is None:
        proc.terminate()
        raise RuntimeError(
            "Neo4j failed to start" + (f": {last_exc!r}" if last_exc else "")
        )

    try:
        with driver.session() as session:
            session.run("CREATE (p:Person {name: 'Alice', age: 36})")
            result = session.run("MATCH (p:Person {name: 'Alice'}) RETURN p.name, p.age")
            record = result.single()
            print("Found:", record["p.name"], "age", record["p.age"])
    finally:
        proc.terminate()
        proc.wait(timeout=30)
        if driver is not None:
            driver.close()


if __name__ == "__main__":
    main()
