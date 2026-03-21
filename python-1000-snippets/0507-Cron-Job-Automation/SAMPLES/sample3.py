# sample3.py
# Log cron-like job completions to temp file.

import datetime
import os
import time

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0507_cron_log.txt')


def job(name):
    return f'{datetime.datetime.now()}: {name} executed\n'


if __name__ == '__main__':
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        for i in range(5):
            f.write(job(f'cron{i}'))
            time.sleep(0.1)
    print('Cron job log written to', OUTPUT_PATH)
