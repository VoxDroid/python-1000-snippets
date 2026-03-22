# sample1.py
# Bulkhead isolation via separate thread pools for types of tasks.

from concurrent.futures import ThreadPoolExecutor


def task_a(i):
    return f'A-{i}'


def task_b(i):
    return f'B-{i}'


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as pool_a, ThreadPoolExecutor(max_workers=1) as pool_b:
        res_a = pool_a.map(task_a, range(4))
        res_b = pool_b.map(task_b, range(3))
        print('A results:', list(res_a))
        print('B results:', list(res_b))
