# sample1.py
# Basic producer-consumer using queue

import threading
import queue
import time

q = queue.Queue()

def producer():
    for i in range(5):
        q.put(i)
        print(f'Produced {i}')
        time.sleep(0.1)

def consumer():
    while True:
        item = q.get()
        print(f'Consumed {item}')
        q.task_done()
        time.sleep(0.2)

if __name__ == '__main__':
    p = threading.Thread(target=producer)
    c = threading.Thread(target=consumer, daemon=True)
    p.start()
    c.start()
    p.join()
    q.join()
    print('Done')
