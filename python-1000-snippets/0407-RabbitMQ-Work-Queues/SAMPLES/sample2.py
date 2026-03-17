# sample2.py
# Demonstrates processing a queue in a worker loop and acknowledging messages.

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
        producer.publish({"task": "cleanup"}, exchange=exchange, routing_key="work")
        producer.publish({"task": "process"}, exchange=exchange, routing_key="work")

        def handle(body, message):
            print("Handling task:", body)
            message.ack()

        with conn.Consumer(queue, callbacks=[handle]):
            # Drain two messages, then stop
            for _ in range(2):
                conn.drain_events(timeout=1)


if __name__ == "__main__":
    main()
