# sample2.py
# Simulate I/O-bound tasks with sleep in a thread pool.

import time
from concurrent.futures import ThreadPoolExecutor


def io_task(x):
    time.sleep(0.1)
    return f'task-{x}-done'


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(io_task, range(10)))
    print('I/O bound results:', results)
