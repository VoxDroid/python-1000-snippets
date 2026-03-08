# sample2.py
# Handler for SIGTERM (e.g., kill)

import signal
import time
import os

def term_handler(signum, frame):
    print('received SIGTERM, shutting down')
    exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, term_handler)
    print('pid', os.getpid(), 'run and send SIGTERM or timeout')
    while True:
        time.sleep(1)
