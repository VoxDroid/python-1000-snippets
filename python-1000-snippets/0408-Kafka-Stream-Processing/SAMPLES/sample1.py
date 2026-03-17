# sample1.py
# Demonstrates producing and consuming a Kafka message using confluent-kafka.

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
    from confluent_kafka import Producer, Consumer, KafkaException

    bootstrap_servers = "localhost:9092"
    topic = "python-snippet-topic"

    producer = Producer({"bootstrap.servers": bootstrap_servers})

    def delivery_report(err, msg):
        if err:
            print("Delivery failed:", err)
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    try:
        producer.produce(topic, key="key", value="Hello Kafka", callback=delivery_report)
        producer.flush(5)
    except KafkaException as e:
        print("Kafka producer error (is Kafka running at", bootstrap_servers, "?):", e)
        return

    consumer = Consumer({
        "bootstrap.servers": bootstrap_servers,
        "group.id": "python-snippet-group",
        "auto.offset.reset": "earliest",
    })

    try:
        consumer.subscribe([topic])
        msg = consumer.poll(timeout=5.0)
        if msg is None:
            print("No message received (broker might be unavailable or topic empty)")
        elif msg.error():
            print("Consumer error:", msg.error())
        else:
            print("Received message:", msg.value().decode())
    except KafkaException as e:
        print("Kafka consumer error (is Kafka running at", bootstrap_servers, "?):", e)
    finally:
        consumer.close()


if __name__ == "__main__":
    main()
