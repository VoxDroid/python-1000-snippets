# sample1.py
# Basic Kafka consumer: poll for one message and exit.
from confluent_kafka import Consumer, KafkaException


def create_consumer():
    return Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'python-group',
        'auto.offset.reset': 'earliest',
    })


if __name__ == '__main__':
    consumer = create_consumer()
    consumer.subscribe(['test-topic'])

    try:
        msg = consumer.poll(timeout=5.0)
        if msg is None:
            print('No message received (timeout)')
        elif msg.error():
            print('Consumer error:', msg.error())
        else:
            print('Received:', msg.value().decode())
    except KafkaException as e:
        print('Kafka error:', e)
    except Exception as e:
        print('Unexpected error:', e)
    finally:
        consumer.close()
