# sample1.py
# Compute squares in parallel using ThreadPoolExecutor.

from concurrent.futures import ThreadPoolExecutor, as_completed


def task(x):
    return x * x


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(task, i) for i in range(10)]
        results = [f.result() for f in as_completed(futures)]
    print('Squared values:', sorted(results))
