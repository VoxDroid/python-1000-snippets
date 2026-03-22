# sample3.py
# Log canary release run to temp output.

import os
from random import random

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0546_canary.txt'))


def log_canary_run(total=100, canary_rate=0.1):
    canary = sum(1 for _ in range(total) if random() < canary_rate)
    stats = {'total': total, 'canary': canary, 'stable': total - canary}
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(str(stats) + '\n')
    return stats


if __name__ == '__main__':
    s = log_canary_run()
    print('Logged:', s)
    print('Path:', OUTPUT_PATH)
