# sample3.py
# demonstrate producer and consumer running sequentially in script
import pika
import time

try:
    conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    ch = conn.channel()
    ch.queue_declare(queue='sample3_queue')
    ch.basic_publish(exchange='', routing_key='sample3_queue', body='msg from producer')
    print('Produced message')
    # consume
    method, prop, body = ch.basic_get('sample3_queue', auto_ack=True)
    if method:
        print('Consumed:', body.decode())
    conn.close()
except Exception as exc:
    print('Error during sample3 run:', exc)

