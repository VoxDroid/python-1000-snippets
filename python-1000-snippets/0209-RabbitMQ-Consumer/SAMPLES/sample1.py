# sample1.py
# publish a message then consume it with a callback (auto_ack)
import pika

try:
    conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    ch = conn.channel()
    ch.queue_declare(queue='sample_queue')
    # publish a message so the consumer has something to read
    ch.basic_publish(exchange='', routing_key='sample_queue', body='hello consumer')
    
    def callback(ch, method, properties, body):
        print('Callback received:', body.decode())
        ch.stop_consuming()
    
    ch.basic_consume(queue='sample_queue', on_message_callback=callback, auto_ack=True)
    print('Waiting for message...')
    ch.start_consuming()
    conn.close()
except Exception as e:
    print('Consumer error:', e)

