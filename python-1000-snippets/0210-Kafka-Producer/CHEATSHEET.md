# 0210-Kafka-Producer Cheatsheet

* Install Python client: `pip install confluent-kafka`.
* Kafka broker must be running (default localhost:9092) before producing.
* Create producer: `Producer({'bootstrap.servers': 'localhost:9092'})`.
* Use `producer.produce(topic, value=...)` to send a message; it’s asynchronous.
* Provide a delivery callback to confirm message delivery or detect errors.
* Call `producer.flush(timeout)` to wait for all queued messages to be delivered.
* To send keys, use `producer.produce(topic, key='k', value='v')`.
* Common errors: `KafkaError._ALL_BROKERS_DOWN`, `KafkaError._MSG_TIMED_OUT`.
* To produce to a specific partition: `producer.produce(topic, value, partition=0)`.
* For high throughput, batch messages and adjust `linger.ms`, `batch.num.messages`.
* Example delivery callback:
  ```python
  def delivery_report(err, msg):
      if err:
          print('Delivery failed:', err)
      else:
          print('Delivered to', msg.topic(), msg.partition())
  ```
