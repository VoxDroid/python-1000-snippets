# sample2.py
# Demonstrates multiple subscribers receiving the same published message.

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


def get_client():
    redis = ensure_redis()
    try:
        client = redis.Redis(host="localhost", port=6379, socket_connect_timeout=1)
        client.ping()
        return client
    except Exception:
        fakeredis = ensure_fakeredis()
        return fakeredis.FakeRedis()


def main() -> None:
    client = get_client()

    pubsub1 = client.pubsub(ignore_subscribe_messages=True)
    pubsub2 = client.pubsub(ignore_subscribe_messages=True)
    pubsub1.subscribe("channel")
    pubsub2.subscribe("channel")

    client.publish("channel", "broadcast")

    msg1 = pubsub1.get_message(timeout=1)
    msg2 = pubsub2.get_message(timeout=1)

    print("Subscriber 1 received:", msg1["data"].decode() if msg1 else None)
    print("Subscriber 2 received:", msg2["data"].decode() if msg2 else None)


if __name__ == "__main__":
    main()
