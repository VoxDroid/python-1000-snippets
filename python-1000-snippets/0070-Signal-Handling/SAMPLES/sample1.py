# sample1.py
# Basic handler for SIGINT (Ctrl+C)

import signal
import time

def handler(signum, frame):
    print('caught SIGINT, exiting')
    exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler)
    print('running, press Ctrl+C or timeout')
    while True:
        time.sleep(1)
