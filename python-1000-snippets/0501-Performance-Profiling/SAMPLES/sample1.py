# sample1.py
# Profile a compute-bound loop with cProfile.

import cProfile


def compute_work(iterations=100000):
    total = 0
    for i in range(iterations):
        total += (i ^ (i << 1)) % 97
    return total


if __name__ == '__main__':
    print('Profiling compute_work...')
    cProfile.run('compute_work(100000)')
