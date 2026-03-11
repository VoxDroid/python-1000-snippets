# sample1.py
# connect to local RabbitMQ, declare queue, publish and then consume one message
import pika

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='test_queue')
    channel.basic_publish(exchange='', routing_key='test_queue', body='hello from sample1')
    print('Message sent')
    method_frame, header_frame, body = channel.basic_get('test_queue', auto_ack=True)
    if method_frame:
        print('Consumed message:', body.decode())
    connection.close()
except pika.exceptions.AMQPConnectionError as e:
    print('Could not connect to RabbitMQ:', e)
    print('Make sure rabbitmq-server is running (sudo systemctl start rabbitmq-server)')
except ImportError:
    print('pika not installed; install with pip install pika')

