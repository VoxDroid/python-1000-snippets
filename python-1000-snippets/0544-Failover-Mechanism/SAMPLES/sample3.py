# sample3.py
# Log failover events.

import os

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0544_failover.log'))


def log_failover(server):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'a') as f:
        f.write(f'active: {server}\n')


if __name__ == '__main__':
    log_failover('backup')
    print('Logged failover to', OUTPUT_PATH)
