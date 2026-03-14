# sample3.py
# Use a consumer that prints partition/offset information and stops after a few messages.
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
    received = 0

    try:
        while received < 2:
            msg = consumer.poll(timeout=5.0)
            if msg is None:
                print('No message received (timeout)')
                continue
            if msg.error():
                print('Consumer error:', msg.error())
                continue
            print(
                'Received:',
                msg.value().decode(),
                'partition',
                msg.partition(),
                'offset',
                msg.offset(),
            )
            received += 1
    except KafkaException as e:
        print('Kafka error:', e)
    except Exception as e:
        print('Unexpected error:', e)
    finally:
        consumer.close()
