# sample1.py
# Demonstrates Redis pub/sub, falling back to fakeredis if no Redis server is running.

import subprocess
import sys


def ensure_redis():
    try:
        import redis  # type: ignore
        return redis
    except ImportError:
        print("Missing dependency: redis. Install with: python -m pip install redis")
        sys.exit(1)


def ensure_fakeredis():
    try:
        import fakeredis  # type: ignore
        return fakeredis
    except ImportError:
        print("Missing dependency: fakeredis. Install with: python -m pip install fakeredis")
        sys.exit(1)


def main() -> None:
    redis = ensure_redis()
    try:
        client = redis.Redis(host="localhost", port=6379, socket_connect_timeout=1)
        client.ping()
        backend = "redis"
    except Exception:  # pragma: no cover
        fakeredis = ensure_fakeredis()
        client = fakeredis.FakeRedis()
        backend = "fakeredis"

    pubsub = client.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe("channel")

    client.publish("channel", "Hello")

    message = pubsub.get_message(timeout=1)
    if message:
        print("Received:", message["data"].decode() if isinstance(message["data"], bytes) else message["data"])
    else:
        print("No message received")

    print("Backend used:", backend)


if __name__ == "__main__":
    main()
