# sample3.py
# Demonstrates pattern-based subscriptions with `psubscribe`.

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

    pubsub = client.pubsub(ignore_subscribe_messages=True)
    pubsub.psubscribe("news.*")

    client.publish("news.sports", "go team")
    client.publish("news.weather", "sunny")

    # Read two messages for the pattern subscription.
    for _ in range(2):
        msg = pubsub.get_message(timeout=1)
        if msg:
            print("Pattern message:", msg["channel"].decode(), msg["data"].decode())


if __name__ == "__main__":
    main()
