# sample1.py
# Basic thread creation demonstration

import threading
import time

def worker(name):
    print(f"Thread {name} starting")
    time.sleep(1)
    print(f"Thread {name} finished")

if __name__ == '__main__':
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('All threads completed')
