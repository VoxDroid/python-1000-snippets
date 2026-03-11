# sample3.py
# run producer in background thread while consumer listens
import pika
import threading
import time

def producer():
    conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    ch = conn.channel()
    ch.queue_declare(queue='concurrent_queue')
    time.sleep(0.2)
    ch.basic_publish(exchange='', routing_key='concurrent_queue', body='msg from producer')
    conn.close()

def consumer():
    conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    ch = conn.channel()
    ch.queue_declare(queue='concurrent_queue')
    
    def cb(ch, method, props, body):
        print('Concurrent consumer got', body.decode())
        ch.stop_consuming()
    
    ch.basic_consume(queue='concurrent_queue', on_message_callback=cb, auto_ack=True)
    ch.start_consuming()
    conn.close()

if __name__ == '__main__':
    t = threading.Thread(target=producer)
    t.start()
    consumer()
    t.join()

