# sample1.py
# Simple chaos engineering scenario with random failure injection.

import random


def chaos_test():
    if random.random() < 0.3:
        raise RuntimeError('Injected chaos failure')
    return 'Success'


if __name__ == '__main__':
    try:
        print('Result:', chaos_test())
    except RuntimeError as e:
        print('Caught failure:', e)
