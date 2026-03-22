# sample2.py
# Evaluate canary traffic percentage over sample requests.

import random


def canary_stats(total=1000, canary_rate=0.1):
    canary = sum(1 for _ in range(total) if random.random() < canary_rate)
    return {'total': total, 'canary': canary, 'stable': total - canary}


if __name__ == '__main__':
    print('Stats:', canary_stats())
