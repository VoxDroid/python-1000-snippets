# sample2.py
# Use multiprocessing to simulate distributed task execution.

from multiprocessing import Pool


def task_pair(pair):
    x, y = pair
    return x + y


if __name__ == '__main__':
    pairs = [(1,2), (3,4), (5,6), (7,8)]
    with Pool(processes=2) as pool:
        results = pool.map(task_pair, pairs)
    print('Distributed-style results:', results)
