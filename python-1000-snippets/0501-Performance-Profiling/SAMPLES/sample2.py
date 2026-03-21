# sample2.py
# Measure execution time using time.perf_counter.

import time


def compute_work(iterations=100000):
    s = 0
    for i in range(iterations):
        s += (i ^ (i << 1)) % 97
    return s


if __name__ == '__main__':
    start = time.perf_counter()
    result = compute_work(100000)
    elapsed = time.perf_counter() - start
    print(f'Result {result} computed in {elapsed:.4f} seconds')
