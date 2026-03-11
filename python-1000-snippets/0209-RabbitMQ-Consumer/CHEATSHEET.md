# 0209-RabbitMQ-Consumer Cheatsheet

* Install pika: `pip install pika`.
* Connect and declare queue similar to producer: `conn = BlockingConnection(...)`.
* Callback signature: `(channel, method, properties, body)`.
* Use `basic_consume` to register callback and `start_consuming()` to begin loop.
* `auto_ack=True` automatically acknowledges messages; otherwise call `ch.basic_ack()`.
* To stop after one message, call `ch.stop_consuming()` inside callback.
* For batch consumption, use `for method, properties, body in ch.consume(queue)`.
* Use `basic_get` for polling-based consumption instead of callback.
* Example manual ack allows requeueing by not acknowledging.
* Use separate threads or processes for producer/consumer for concurrency (see sample3).
* Handle `pika.exceptions.AMQPConnectionError` when broker unreachable.
* To prefetch N messages, `ch.basic_qos(prefetch_count=N)`.
* Closing connection gracefully ensures unacknowledged messages are requeued.
* Use durable queues and persistent messages to survive broker restarts.
* Example snippet to start consumer: `ch.basic_consume('queue', callback, auto_ack=True)`.
