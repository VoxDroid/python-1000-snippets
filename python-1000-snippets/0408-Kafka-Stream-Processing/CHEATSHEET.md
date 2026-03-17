# 0408-Kafka-Stream-Processing Cheatsheet

- Install `confluent-kafka` with `python -m pip install confluent-kafka`.
- Create a `Producer` with `Producer({"bootstrap.servers": "localhost:9092"})`.
- Create a `Consumer` with `Consumer({"bootstrap.servers": ..., "group.id": ...})`.
- Use `consumer.poll(timeout=...)` to retrieve messages.
- If no broker is running, the script will print an error message.
