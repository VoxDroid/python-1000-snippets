# sample2.py
# manual ack example
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
ch = conn.channel()
ch.queue_declare(queue='manual_ack_queue')
ch.basic_publish(exchange='', routing_key='manual_ack_queue', body='please ack')

def callback(ch, method, properties, body):
    print('Manual ack received:', body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)
    ch.stop_consuming()

ch.basic_consume(queue='manual_ack_queue', on_message_callback=callback, auto_ack=False)
print('Waiting for manual ack...')
ch.start_consuming()
conn.close()

