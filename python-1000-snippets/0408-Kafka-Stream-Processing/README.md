# Kafka Stream Processing

## Description
Demonstrates producing and consuming messages using `confluent-kafka`. The script attempts to connect to a Kafka broker at `localhost:9092`.

## Files
- `SAMPLES/sample1.py` — Produces a message and consumes it from the same topic.
- `SAMPLES/sample2.py` — (placeholder) could show partitioning or key-based routing.
- `SAMPLES/sample3.py` — (placeholder) could show consumer groups.

## Usage
```bash
python SAMPLES/sample1.py
```

## Notes
- The script installs `confluent-kafka` if missing.
- A local Kafka broker must be running at `localhost:9092` for the sample to succeed.

## Quick Start (if you have Docker)
```bash
docker run -d --name kafka -p 9092:9092 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 -e KAFKA_ZOOKEEPER_CONNECT=localhost:2181 wurstmeister/kafka
```
