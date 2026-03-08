# sample2.py
# Demonstrate timeout when queue is empty

import queue
import threading
import time

q = queue.Queue()

def consumer():
    try:
        item = q.get(timeout=1)
        print('got', item)
    except queue.Empty:
        print('queue was empty, timed out')

if __name__ == '__main__':
    t = threading.Thread(target=consumer)
    t.start()
    t.join()
