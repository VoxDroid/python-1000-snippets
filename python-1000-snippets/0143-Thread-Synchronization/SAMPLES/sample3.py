# sample3.py
# demonstrate use of RLock for recursive locking

import threading

rlock = threading.RLock()

count = 0

def recursive(depth):
    global count
    with rlock:
        count += 1
        if depth > 0:
            recursive(depth-1)

if __name__ == '__main__':
    recursive(5)
    print('count', count)
