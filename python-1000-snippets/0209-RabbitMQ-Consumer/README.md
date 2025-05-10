# RabbitMQ Consumer

## Description
This snippet demonstrates a RabbitMQ consumer using `pika` to receive messages.

## Prerequisites
- Install RabbitMQ: Follow instructions at [RabbitMQ Installation](https://www.rabbitmq.com/download.html).
- Start RabbitMQ server: `sudo systemctl start rabbitmq` (Linux) or `rabbitmq-server` (macOS/Windows).
- Install `pika`: `pip install pika`.
- Ensure `localhost:5672` is accessible (default RabbitMQ port).

## Code
```python
# Note: Requires `pika`. Install with `pip install pika`
try:
    import pika
    def callback(ch, method, properties, body):
        print(f"Received: {body.decode()}")
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="my_queue")
    channel.basic_consume(queue="my_queue", on_message_callback=callback, auto_ack=True)
    print("Waiting for messages...")
    channel.start_consuming()
except ImportError:
    print("Mock Output: Received: Hello, RabbitMQ!")
```

## Output
```
Mock Output: Received: Hello, RabbitMQ!
```
*(Real output with RabbitMQ: `Waiting for messages... Received: Hello, RabbitMQ!`)*

## Explanation
- **RabbitMQ Consumer**: Receives messages from a queue using `pika`.
- **Logic**: Declares a queue and consumes messages with `basic_consume`.
- **Complexity**: O(1) per message (network latency varies).
- **Use Case**: Used for processing tasks or events in distributed systems.
- **Best Practice**: Handle message acknowledgments; manage connection lifecycle; scale consumers.