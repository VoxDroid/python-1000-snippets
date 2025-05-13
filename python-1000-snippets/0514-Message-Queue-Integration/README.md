# Message Queue Integration

## Description
This snippet demonstrates sending a message to RabbitMQ using `pika`.

## Code
```python
# Note: Requires `pika`. Install with `pip install pika`
try:
    import pika
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="test")
    print("Queue declared")
    connection.close()
except ImportError:
    print("Mock Output: Queue declared")
```

## Output
```
Mock Output: Queue declared
```
*(Real output with `pika`: `Queue declared`)*

## Explanation
- **Message Queue Integration**: Sets up a RabbitMQ queue.
- **Logic**: Declares a queue using `pika`.
- **Complexity**: O(1) for setup (network-dependent).
- **Use Case**: Used for asynchronous task processing.
- **Best Practice**: Handle connection errors; use durable queues; monitor queues.