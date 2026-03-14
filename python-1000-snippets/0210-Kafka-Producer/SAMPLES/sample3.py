# sample3.py
# Produce a message to a specific partition and handle delivery asynchronously.
from confluent_kafka import Producer, KafkaException


def delivery_report(err, msg):
    if err:
        print('Delivery failed:', err)
    else:
        print('Delivered to', msg.topic(), 'partition', msg.partition(), 'offset', msg.offset())


if __name__ == '__main__':
    producer = Producer({'bootstrap.servers': 'localhost:9092'})

    try:
        producer.produce('test-topic', value='partitioned', partition=0, callback=delivery_report)
        producer.flush(10)
    except KafkaException as e:
        print('Kafka error:', e)
    except Exception as e:
        print('Unexpected error:', e)

