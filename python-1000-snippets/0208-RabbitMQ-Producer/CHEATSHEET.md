# 0208-RabbitMQ-Producer Cheatsheet

* Install pika with `pip install pika`.
* Connect: `connection = pika.BlockingConnection(pika.ConnectionParameters(host))`.
* Channel: `channel = connection.channel()`.
* Declare queue: `channel.queue_declare(queue='name', durable=True)` (durable persists across broker restarts).
* Publish: `channel.basic_publish(exchange='', routing_key='queue', body='msg', properties=pika.BasicProperties(...))`.
* Make message persistent: `BasicProperties(delivery_mode=2)`.
* To send to exchange use `exchange='my_ex'` and routing_key accordingly.
* Close connection with `connection.close()`.
* To consume, use `channel.basic_consume(queue, callback)` or `basic_get` for one-off.
* Handle `pika.exceptions.AMQPConnectionError` when broker unavailable.
* Default port: 5672; use credentials via `pika.PlainCredentials('user','pass')`.
* For SSL: `pika.ConnectionParameters(host, ssl_options=...)`.
* Use QoS with `channel.basic_qos(prefetch_count=1)` to limit unacked messages.
* Best practice: declare queue on both producer and consumer; handle channel exceptions; use selective acknowledgments.
* Example quick publish/consume in one script (see samples).
