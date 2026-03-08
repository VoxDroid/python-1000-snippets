# sample3.py
# Ignore SIGINT temporarily

import signal
import time

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    print('SIGINT ignored for 3 seconds')
    time.sleep(3)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    print('SIGINT back to default, press Ctrl+C to exit')
    while True:
        time.sleep(1)
