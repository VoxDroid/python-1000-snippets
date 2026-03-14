# sample2.py
# Consume messages in a loop and commit offsets manually.
from confluent_kafka import Consumer, KafkaException


def create_consumer():
    return Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'python-group',
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': False,
    })


if __name__ == '__main__':
    consumer = create_consumer()
    consumer.subscribe(['test-topic'])
    try:
        for _ in range(3):
            msg = consumer.poll(timeout=5.0)
            if msg is None:
                print('No message received (timeout)')
                continue
            if msg.error():
                print('Consumer error:', msg.error())
                continue
            print('Received:', msg.value().decode())
            consumer.commit(message=msg)
    except KafkaException as e:
        print('Kafka error:', e)
    except Exception as e:
        print('Unexpected error:', e)
    finally:
        consumer.close()
