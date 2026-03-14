# 0211-Kafka-Consumer Cheatsheet

* Install with `pip install confluent-kafka`.
* Configure consumer with `bootstrap.servers`, `group.id`, and `auto.offset.reset`.
* Use `consumer.subscribe([topic])` or `consumer.assign([TopicPartition(topic, partition)])`.
* Use `consumer.poll(timeout)` to retrieve messages; handle `None` or errors.
* Call `consumer.commit()` to commit offsets (auto-commit can be enabled with `enable.auto.commit`).
* Always call `consumer.close()` when done to leave the group cleanly.
* Typical patterns: loop polling until a stop condition, break on Ctrl+C.
* Use `consumer.seek()` to rewind offsets, or use `auto.offset.reset` to control start position.
* For high throughput, tune `fetch.min.bytes`, `fetch.max.wait.ms`, `max.partition.fetch.bytes`.
* Use `confluent_kafka.KafkaError._PARTITION_EOF` to detect end-of-partition.

