# sample3.py
# Demonstrates a simple consumer group with multiple consumers.

import subprocess
import sys


def ensure_confluent_kafka():
    try:
        import confluent_kafka  # type: ignore
        return confluent_kafka
    except ImportError:
        print("Missing dependency: confluent-kafka. Install with: python -m pip install confluent-kafka")
        sys.exit(1)


def consume_once(group_id: str):
    confluent_kafka = ensure_confluent_kafka()
    from confluent_kafka import Consumer, KafkaException

    bootstrap_servers = "localhost:9092"
    topic = "python-snippet-topic"

    consumer = Consumer({
        "bootstrap.servers": bootstrap_servers,
        "group.id": group_id,
        "auto.offset.reset": "earliest",
    })

    consumer.subscribe([topic])
    try:
        msg = consumer.poll(timeout=5.0)
        if msg is None:
            print(f"{group_id}: No message (broker may be down or no new data)")
        elif msg.error():
            print(f"{group_id}: Consumer error:", msg.error())
        else:
            print(f"{group_id}: Received {msg.value().decode()} (key={msg.key()})")
    except KafkaException as e:
        print(f"{group_id}: Kafka error (is broker running?):", e)
    finally:
        consumer.close()


def main() -> None:
    # Run two consumers in the same process sequentially to demonstrate group behavior.
    consume_once("group-1")
    consume_once("group-2")


if __name__ == "__main__":
    main()
