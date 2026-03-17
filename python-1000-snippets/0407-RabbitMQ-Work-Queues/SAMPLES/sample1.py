# sample1.py
# Demonstrates a work queue using Kombu's in-memory transport.

import subprocess
import sys


def ensure_kombu():
    try:
        import kombu  # type: ignore
        return kombu
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "kombu"])  # nosec
        import kombu  # type: ignore
        return kombu


def main() -> None:
    kombu = ensure_kombu()
    from kombu import Connection, Exchange, Queue

    exchange = Exchange("tasks", type="direct")
    queue = Queue("work", exchange, routing_key="work")

    with Connection("memory://") as conn:
        producer = conn.Producer()
        producer.publish({"task": "process"}, exchange=exchange, routing_key="work")

        with conn.Consumer(queue, callbacks=[lambda body, message: print('Received:', body) or message.ack()]):
            conn.drain_events(timeout=1)


if __name__ == "__main__":
    main()
