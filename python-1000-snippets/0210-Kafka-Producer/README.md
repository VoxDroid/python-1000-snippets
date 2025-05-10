# Kafka Producer

## Description
This snippet demonstrates a Kafka producer using `confluent-kafka` to send messages.

## Code
```python
# Note: Requires `confluent-kafka`. Install with `pip install confluent-kafka`
try:
    from confluent_kafka import Producer
    config = {"bootstrap.servers": "localhost:9092"}
    producer = Producer(config)
    producer.produce("my_topic", value="Hello, Kafka!".encode())
    producer.flush()
    print("Message sent")
except ImportError:
    print("Mock Output: Message sent: Hello, Kafka!")
```

## Output
```
Mock Output: Message sent: Hello, Kafka!
```
*(Real output with Kafka: `Message sent`)*

## Explanation
- **Kafka Producer**: Sends a message to a Kafka topic using `confluent-kafka`.
- **Logic**: Configures a producer and sends a message with `produce`.
- **Complexity**: O(1) for sending (network latency varies).
- **Use Case**: Used for streaming data or event-driven architectures.
- **Best Practice**: Handle delivery errors; configure retries; ensure Kafka broker is running.