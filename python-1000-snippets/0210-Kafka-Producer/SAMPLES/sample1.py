# sample1.py
# Basic Kafka producer: send a single message and wait for delivery.
from confluent_kafka import Producer, KafkaException


def delivery_report(err, msg):
    if err is not None:
        print('Delivery failed:', err)
    else:
        print('Message delivered to', msg.topic(), 'partition', msg.partition())


if __name__ == '__main__':
    config = {'bootstrap.servers': 'localhost:9092'}
    producer = Producer(config)

    try:
        producer.produce('test-topic', value='Hello, Kafka!', callback=delivery_report)
        producer.flush(10)
    except KafkaException as e:
        print('Kafka error:', e)
    except Exception as e:
        print('Unexpected error:', e)

