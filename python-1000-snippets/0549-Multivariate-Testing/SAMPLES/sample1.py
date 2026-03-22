# sample1.py
# Assign variants for multiple test dimensions.

import random

VARIANTS = {
    'color': ['red', 'blue'],
    'size': ['small', 'large']
}


def assign_variants():
    return {k: random.choice(v) for k, v in VARIANTS.items()}


if __name__ == '__main__':
    print('Assigned variants:', assign_variants())
