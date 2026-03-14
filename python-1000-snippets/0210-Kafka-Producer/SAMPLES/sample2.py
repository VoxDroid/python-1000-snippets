# sample2.py
# Send multiple messages in a loop with keys and flush.
from confluent_kafka import Producer, KafkaException


def delivery_report(err, msg):
    if err:
        print('Delivery failed:', err)
    else:
        print('Delivered message to', msg.topic(), 'partition', msg.partition(), 'offset', msg.offset())


if __name__ == '__main__':
    producer = Producer({'bootstrap.servers': 'localhost:9092'})

    try:
        for i in range(3):
            producer.produce('test-topic', key=str(i), value=f'message {i}', callback=delivery_report)
        producer.flush(10)
    except KafkaException as e:
        print('Kafka error:', e)
    except Exception as e:
        print('Unexpected error:', e)

