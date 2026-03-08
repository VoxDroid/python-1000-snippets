# sample3.py
# Simple thread pool using queue

import threading
import queue

def worker(q):
    while True:
        func, args = q.get()
        if func is None:
            break
        func(*args)
        q.task_done()

def task(n):
    print('task', n)

if __name__ == '__main__':
    q = queue.Queue()
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(q,))
        t.start()
        threads.append(t)
    for i in range(5):
        q.put((task, (i,)))
    q.join()
    for _ in threads:
        q.put((None, ()))
    for t in threads:
        t.join()
    print('all tasks done')
