# sample2.py
# Generate CPU-bound task durations using process pool.

import time
from concurrent.futures import ProcessPoolExecutor


def busy_task(seconds):
    start = time.time()
    while time.time() - start < seconds:
        _ = sum(i*i for i in range(1000))
    return f'done in {seconds}s'


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(busy_task, [0.2, 0.2, 0.2]))
    print('Process task results:', results)
