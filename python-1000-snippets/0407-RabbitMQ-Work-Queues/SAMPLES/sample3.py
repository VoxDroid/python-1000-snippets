# sample3.py
# Demonstrates using exchanges and routing keys to deliver messages to different queues.

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

    exchange = Exchange("logs", type="direct")
    info_queue = Queue("info", exchange, routing_key="info")
    error_queue = Queue("error", exchange, routing_key="error")

    with Connection("memory://") as conn:
        producer = conn.Producer()
        producer.publish({"level": "info", "msg": "Info message"}, exchange=exchange, routing_key="info")
        producer.publish({"level": "error", "msg": "Error message"}, exchange=exchange, routing_key="error")

        def print_msg(prefix):
            def handler(body, message):
                print(f"{prefix}:", body)
                message.ack()

            return handler

        with conn.Consumer(info_queue, callbacks=[print_msg("INFO")]):
            conn.drain_events(timeout=1)

        with conn.Consumer(error_queue, callbacks=[print_msg("ERROR")]):
            conn.drain_events(timeout=1)


if __name__ == "__main__":
    main()
