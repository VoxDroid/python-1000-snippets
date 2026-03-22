# sample2.py
# Compute experiment bucket distribution for N users and desired split.

import random


def simulate_ab(n=1000, a_ratio=0.5):
    counts = {'A': 0, 'B': 0}
    for _ in range(n):
        variant = 'A' if random.random() < a_ratio else 'B'
        counts[variant] += 1
    return counts


if __name__ == '__main__':
    print('Simulated assignment:', simulate_ab())
