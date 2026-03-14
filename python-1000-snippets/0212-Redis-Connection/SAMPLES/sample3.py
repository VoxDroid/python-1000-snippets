# sample3.py
# Pub/Sub example using redis-py
import threading
import time
import redis


def subscriber():
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    pubsub = r.pubsub()
    pubsub.subscribe('mychannel')
    for msg in pubsub.listen():
        if msg['type'] == 'message':
            print('Received:', msg['data'])
            break


if __name__ == '__main__':
    thread = threading.Thread(target=subscriber, daemon=True)
    thread.start()
    time.sleep(0.5)
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    r.publish('mychannel', 'hello pubsub')
    thread.join(timeout=2)

