# Message Queue Integration

## Description
This snippet demonstrates message queue integration patterns with local queue simulation and optional RabbitMQ.

## Code
- `SAMPLES/sample1.py`: local `deque` queue plus optional `pika` RabbitMQ connection check.
- `SAMPLES/sample2.py`: producer/consumer with log file output to `temp/0514_mq_log.txt`.
- `SAMPLES/sample3.py`: reads queue log and prints count.

## Output
- sample1: local queue consumed and RabbitMQ status.
- sample2: processed entries persisted to temp file.
- sample3: returned log entry count.

## Explanation
- **Message Queue Integration**: demonstrates queue patterns and queue-based persistence.
- **Logic**: use local queue object + attempt to use `pika` if available.
- **Complexity**: O(n) for queue processing.
- **Use Case**: event-driven task orchestration or messaging middleware integration.
- **Best Practice**: use durable queues, handle reconnects, and use acknowledgements in production.
