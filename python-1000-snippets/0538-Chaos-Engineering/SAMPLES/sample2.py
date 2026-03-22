# sample2.py
# Run chaos tests in loop and report success/fail counts.

import random


def chaos_rounds(n):
    success = 0
    failures = 0
    for _ in range(n):
        try:
            if random.random() < 0.2:
                raise RuntimeError('failure')
            success += 1
        except RuntimeError:
            failures += 1
    return {'success': success, 'failures': failures}


if __name__ == '__main__':
    print(chaos_rounds(5))
