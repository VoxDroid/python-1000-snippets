# sample3.py
# Log replication status to temp file.

import os

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0542_replication.txt'))


def log_replication(status):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(status + '\n')


if __name__ == '__main__':
    log_replication('replica sync complete')
    print('Logged replication status to', OUTPUT_PATH)
