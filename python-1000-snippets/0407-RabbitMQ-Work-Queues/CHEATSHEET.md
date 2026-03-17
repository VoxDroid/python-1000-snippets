# 0407-RabbitMQ-Work-Queues Cheatsheet

- Install `kombu` with `python -m pip install kombu`.
- Use `Connection('memory://')` for in-memory demonstration without a broker.
- Use `Exchange` and `Queue` to declare message routing.
- Use `Producer.publish()` to send messages and `Consumer` with callbacks to receive.
- Acknowledge messages via `message.ack()` to simulate work queue semantics.
