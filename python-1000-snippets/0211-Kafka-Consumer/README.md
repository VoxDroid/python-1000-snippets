# Kafka Consumer

## Description
This snippet demonstrates a Kafka consumer using `confluent-kafka` to receive messages from a topic.

## Code
```python
# Note: Requires `confluent-kafka`. Install with `pip install confluent-kafka`
try:
    from confluent_kafka import Consumer
    config = {
        "bootstrap.servers": "localhost:9092",
        "group.id": "my-group",
        "auto.offset.reset": "earliest"
    }
    consumer = Consumer(config)
    consumer.subscribe(["my_topic"])
    msg = consumer.poll(1.0)
    if msg:
        print("Received:", msg.value().decode())
    consumer.close()
except ImportError:
    print("Mock Output: Received: Hello, Kafka!")
```

## Output
```
Mock Output: Received: Hello, Kafka!
```
*(Real output with Kafka: `Received: Hello, Kafka!` if a message exists)*

## Explanation
- **Kafka Consumer**: Subscribes to a topic and polls for messages using `confluent-kafka`.
- **Logic**: Configures a consumer, subscribes to `my_topic`, and prints the first message.
- **Complexity**: O(1) per poll (network latency varies).
- **Use Case**: Used for processing streaming data in event-driven systems.
- **Best Practice**: Handle errors; commit offsets; ensure Kafka broker is running.