# sample1.py
# run two threads incrementing a shared counter protected by a lock

import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

if __name__ == '__main__':
    threads = [threading.Thread(target=increment) for _ in range(2)]
    for t in threads: t.start()
    for t in threads: t.join()
    print('Final Counter:', counter)
