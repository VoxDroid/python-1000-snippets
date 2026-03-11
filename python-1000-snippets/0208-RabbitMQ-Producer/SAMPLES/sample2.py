# sample2.py
# publish persistent message to a durable queue
import pika

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='durable_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='durable_queue',
        body='persistent hello',
        properties=pika.BasicProperties(delivery_mode=2)  # make message persistent
    )
    print('Persistent message sent')
    connection.close()
except Exception as e:
    print('Error:', e)

