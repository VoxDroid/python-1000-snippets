# sample2.py
# Use a Lock to synchronize access to a shared counter

import threading

counter = 0
lock = threading.Lock()

def incr():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

if __name__ == '__main__':
    threads = [threading.Thread(target=incr) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('counter should be 5000, got', counter)
