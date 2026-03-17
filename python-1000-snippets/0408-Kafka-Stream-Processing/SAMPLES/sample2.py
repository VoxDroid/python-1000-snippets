# sample2.py
# Demonstrates sending messages with keys to control partitioning.

import subprocess
import sys


def ensure_confluent_kafka():
    try:
        import confluent_kafka  # type: ignore
        return confluent_kafka
    except ImportError:
        print("Missing dependency: confluent-kafka. Install with: python -m pip install confluent-kafka")
        sys.exit(1)


def main() -> None:
    confluent_kafka = ensure_confluent_kafka()
    from confluent_kafka import Producer, KafkaException

    bootstrap_servers = "localhost:9092"
    topic = "python-snippet-topic"

    producer = Producer({"bootstrap.servers": bootstrap_servers})

    def delivery_report(err, msg):
        if err:
            print("Delivery failed:", err)
        else:
            print(f"Delivered to {msg.topic()} [{msg.partition()}]")

    try:
        for key in ["A", "B", "A"]:
            producer.produce(topic, key=key, value=f"message-for-{key}".encode(), callback=delivery_report)
        producer.flush(5)
    except KafkaException as e:
        print("Kafka error (is broker running at", bootstrap_servers, "?):", e)


if __name__ == "__main__":
    main()
