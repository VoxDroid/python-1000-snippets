# RabbitMQ Producer

## Description
This snippet demonstrates a RabbitMQ producer using `pika` to send a message to a queue.

## Prerequisites
- Install RabbitMQ: Follow instructions at [RabbitMQ Installation](https://www.rabbitmq.com/download.html).
- Start RabbitMQ server: `sudo systemctl start rabbitmq` (Linux) or `rabbitmq-server` (macOS/Windows).
- Install `pika`: `pip install pika`.
- Ensure `localhost:5672` is accessible (default RabbitMQ port).

## Code
```python
import pika
import sys

try:
    # Establish connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    
    # Declare a queue
    channel.queue_declare(queue="my_queue")
    
    # Publish a message
    message = "Hello, RabbitMQ!"
    channel.basic_publish(exchange="", routing_key="my_queue", body=message)
    
    print(f"Message sent: {message}")
    
    # Close connection
    connection.close()

except pika.exceptions.AMQPConnectionError:
    print("Error: Failed to connect to RabbitMQ. Ensure the server is running on localhost:5672.")
    print("Start RabbitMQ with: 'sudo systemctl start rabbitmq-server' (Linux) or 'rabbitmq-server' (macOS/Windows).")
    sys.exit(1)
except ImportError:
    print("Mock Output: Message sent: Hello, RabbitMQ!")
    print("Note: Install pika with 'pip install pika' for real execution.")
```

## Output
*(If RabbitMQ is running and `pika` is installed)*
```
Message sent: Hello, RabbitMQ!
```

*(If RabbitMQ server is not running)*
```
Error: Failed to connect to RabbitMQ. Ensure the server is running on localhost:5672.
Start RabbitMQ with: 'sudo systemctl start rabbitmq-server' (Linux) or 'rabbitmq-server' (macOS/Windows).
```

*(If `pika` is not installed)*
```
Mock Output: Message sent: Hello, RabbitMQ!
Note: Install pika with 'pip install pika' for real execution.
```

## Explanation
- **RabbitMQ Producer**: Sends a message to a queue named `my_queue` using `pika`.
- **Logic**: Connects to RabbitMQ on `localhost:5672`, declares a queue, and publishes a message with `basic_publish`.
- **Error Handling**: Catches `AMQPConnectionError` to guide users if the server isn’t running.
- **Complexity**: O(1) for publishing (network latency varies).
- **Use Case**: Used in task queues or message-driven systems for asynchronous processing.
- **Best Practice**:
  - Ensure RabbitMQ is installed and running before executing.
  - Use durable queues for persistence: Add `durable=True` in `queue_declare`.
  - Handle connection errors gracefully in production code.
  - Consider using credentials if RabbitMQ is configured with authentication.
  - Use environment variables for host/port in real applications.

## Troubleshooting
- **AMQPConnectionError**: Verify RabbitMQ is running (`rabbitmqctl status`) and port 5672 is open (`netstat -an | grep 5672`).
- **Connection Refused**: Check firewall settings or ensure `localhost` resolves correctly.
- **Authentication Error**: If `guest` user is restricted, provide credentials in `ConnectionParameters` (e.g., `credentials=pika.PlainCredentials('user', 'pass')`).
- **Queue Not Found**: Ensure the consumer (e.g., Snippet 209) uses the same queue name (`my_queue`).