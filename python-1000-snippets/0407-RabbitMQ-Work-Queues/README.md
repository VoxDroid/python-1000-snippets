# RabbitMQ Work Queues

## Description
This snippet demonstrates a RabbitMQ work queue using `pika`.

## Code
```python
# Note: Requires `pika`. Install with `pip install pika`
try:
    import pika
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="work")
    channel.basic_publish(exchange="", routing_key="work", body="Task")
    print("Task published")
    connection.close()
except ImportError:
    print("Mock Output: Task published")
```

## Output
```
Mock Output: Task published
```
*(Real output with `pika` and RabbitMQ: Publishes to queue)*

## Explanation
- **RabbitMQ Work Queues**: Publishes tasks to a RabbitMQ queue.
- **Logic**: Connects to RabbitMQ, declares a queue, and publishes a message.
- **Complexity**: O(1) per publish.
- **Use Case**: Used for task distribution or background jobs.
- **Best Practice**: Handle connection failures; ensure durability; monitor queues.