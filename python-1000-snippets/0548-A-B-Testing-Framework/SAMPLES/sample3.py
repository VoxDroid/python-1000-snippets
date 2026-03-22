# sample3.py
# Log A/B test stats to temp file.

import os
import random

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0548_ab_test.txt'))


def log_ab_stats(n=100, a_ratio=0.5):
    stats = {'A': 0, 'B': 0}
    for _ in range(n):
        variant = 'A' if random.random() < a_ratio else 'B'
        stats[variant] += 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(str(stats) + '\n')
    return stats


if __name__ == '__main__':
    result = log_ab_stats()
    print('Logged stats:', result)
    print('Path:', OUTPUT_PATH)
