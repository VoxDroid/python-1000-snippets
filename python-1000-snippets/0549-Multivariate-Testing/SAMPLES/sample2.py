# sample2.py
# Simulate N users in multivariate test and count combinations.

import random

VARIANTS = {
    'color': ['red', 'blue'],
    'size': ['small', 'large']
}


def simulate(n=1000):
    counts = {}
    for _ in range(n):
        combo = tuple((k, random.choice(v)) for k, v in VARIANTS.items())
        counts[combo] = counts.get(combo, 0) + 1
    return counts


if __name__ == '__main__':
    result = simulate(200)
    print('Top combinations:', sorted(result.items(), key=lambda x: -x[1])[:3])
