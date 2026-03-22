# sample1.py
# Anonymize a list of names with pseudo-random mapping.

import random


def anonymize_names(names):
    random.seed(42)
    return [f'User{random.randint(1000,9999)}' for _ in names]


if __name__ == '__main__':
    names = ['Alice', 'Bob', 'Charlie']
    anon = anonymize_names(names)
    print('Anonymized names:', anon)
