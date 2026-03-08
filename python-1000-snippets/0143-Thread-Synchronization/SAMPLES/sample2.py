# sample2.py
# show race condition without lock for comparison

import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # no lock

if __name__ == '__main__':
    threads = [threading.Thread(target=increment) for _ in range(2)]
    for t in threads: t.start()
    for t in threads: t.join()
    print('Final Counter (no lock):', counter)
