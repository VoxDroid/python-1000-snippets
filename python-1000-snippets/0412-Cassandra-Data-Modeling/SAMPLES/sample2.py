# sample2.py
# Demonstrates creating a table with a composite primary key and querying by partition.

import os
import shutil
import socket
import subprocess
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
    jars = [cassandra_conf]
    lib_dir = os.path.join(cassandra_home, "lib")
    for jar in sorted(os.listdir(lib_dir)):
        if jar.endswith(".jar"):
            jars.append(os.path.join(lib_dir, jar))
    jsr223_dir = os.path.join(lib_dir, "jsr223")
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
    config["data_file_directories"] = [os.path.join(data_dir, "data")]
    config["commitlog_directory"] = os.path.join(data_dir, "commitlog")
    config["saved_caches_directory"] = os.path.join(data_dir, "saved_caches")
    config["hints_directory"] = os.path.join(data_dir, "hints")

    for path in [
        config["data_file_directories"][0],
        config["commitlog_directory"],
        config["saved_caches_directory"],
        config["hints_directory"],
    ]:
        os.makedirs(path, exist_ok=True)

    # Copy the bundled JVM options and strip out flags that are unsupported by current Java versions.
    for opts in [
        "jvm-server.options",
        "jvm11-server.options",
        "jvm8-server.options",
    ]:
        src_opts = os.path.join(_repo_root(), "cassandra", "conf", opts)
        dst_opts = os.path.join(temp_conf, opts)
        if not os.path.exists(src_opts):
            continue
        shutil.copy(src_opts, dst_opts)

        with open(dst_opts, "r", encoding="utf-8") as f:
            lines = [
                l
                for l in f
                if "UseBiasedLocking" not in l
                and "UseConcMarkSweepGC" not in l
                and "CMS" not in l
            ]
        with open(dst_opts, "w", encoding="utf-8") as f:
            f.writelines(lines)

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

    # Use Java 11 for compatibility with Cassandra 4.x.
    env["JAVA_HOME"] = "/usr/lib/jvm/java-1.11.0-openjdk-amd64"
    env["PATH"] = os.path.join(env["JAVA_HOME"], "bin") + ":" + env.get("PATH", "")

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

    deadline = time.time() + 60
    cluster = None
    while time.time() < deadline:
        cluster = Cluster(["127.0.0.1"], port=port, connect_timeout=1)
        try:
            session = cluster.connect()
            session.execute("SELECT now() FROM system.local")
            break
        except Exception:
            cluster.shutdown()
            cluster = None
            time.sleep(1)

    if cluster is None:
        proc.terminate()
        raise RuntimeError("Cassandra failed to start")

    try:
        session = cluster.connect()
        session.execute("CREATE KEYSPACE IF NOT EXISTS testks WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}")
        session.set_keyspace("testks")
        session.execute(
            "CREATE TABLE IF NOT EXISTS orders (customer_id int, order_id int, amount double, PRIMARY KEY (customer_id, order_id))"
        )

        session.execute("INSERT INTO orders (customer_id, order_id, amount) VALUES (1, 100, 12.5)")
        session.execute("INSERT INTO orders (customer_id, order_id, amount) VALUES (1, 101, 7.75)")
        session.execute("INSERT INTO orders (customer_id, order_id, amount) VALUES (2, 200, 50.0)")

        print("Orders for customer 1:")
        for row in session.execute("SELECT order_id, amount FROM orders WHERE customer_id = 1"):
            print(row)

    finally:
        if cluster is not None:
            cluster.shutdown()
        proc.terminate()
        proc.wait(timeout=10)


if __name__ == "__main__":
    main()
