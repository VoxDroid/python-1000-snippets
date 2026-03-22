# sample3.py
# Record multivariate assignment stats to temp file.

import os
import random

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0549_multivariate.txt'))

VARIANTS = {
    'color': ['red', 'blue'],
    'size': ['small', 'large']
}


def log_multivariate(n=50):
    counts = {}
    for _ in range(n):
        combo = tuple((k, random.choice(v)) for k, v in VARIANTS.items())
        counts[combo] = counts.get(combo, 0) + 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(str(counts) + '\n')
    return counts


if __name__ == '__main__':
    stats = log_multivariate()
    print('For file:', OUTPUT_PATH)
    print({str(k): v for k, v in stats.items()})
