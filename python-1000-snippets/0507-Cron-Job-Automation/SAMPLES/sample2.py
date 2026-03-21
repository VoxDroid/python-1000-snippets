# sample2.py
# Cron-like repeating using while loop and sleep.

import datetime
import time


def job(name):
    print(f'{datetime.datetime.now()}: {name} executed')


if __name__ == '__main__':
    start = time.time()
    while time.time() - start < 1.0:
        job('maintenance')
        time.sleep(0.3)
    print('Cron loop completed')
