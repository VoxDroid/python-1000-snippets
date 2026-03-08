# sample3.py
# Demonstrate daemon threads that exit with main thread

import threading
import time

def background():
    while True:
        print('background running')
        time.sleep(0.5)

if __name__ == '__main__':
    t = threading.Thread(target=background)
    t.daemon = True
    t.start()
    print('main thread sleeping for 2 seconds')
    time.sleep(2)
    print('main thread exiting, daemon thread will stop')
