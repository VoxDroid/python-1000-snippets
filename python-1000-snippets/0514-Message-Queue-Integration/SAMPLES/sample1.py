# sample1.py
# Simulate message queue publish/consume via deque, plus optional RabbitMQ via pika.

from collections import deque


def local_queue_simulation():
    q = deque()
    for i in range(5):
        q.append(f'msg-{i}')
    consumed = []
    while q:
        consumed.append(q.popleft())
    return consumed


def rabbitmq_check():
    try:
        import pika
        conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = conn.channel()
        channel.queue_declare(queue='test')
        channel.close()
        conn.close()
        return 'rabbitmq available'
    except Exception as e:
        return f'rabbitmq not available: {e}'


if __name__ == '__main__':
    print('Local queue consume:', local_queue_simulation())
    print('RabbitMQ status:', rabbitmq_check())
