# sample1.py
# Assign a booked user to variant A or B with given percentage for A.

import random


def assign_variant(a_ratio=0.5):
    return 'A' if random.random() < a_ratio else 'B'


if __name__ == '__main__':
    print('Assigned variant:', assign_variant())
