# sample3.py
# Write thread pool statistics to a temp log file.

import os
from concurrent.futures import ThreadPoolExecutor

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0503_thread_pool.txt')


def task(x):
    return x * x


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(task, range(50)))

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write('Result length: ' + str(len(results)) + '\n')
        f.write('Results sum: ' + str(sum(results)) + '\n')

    print('Wrote thread pool summary to', OUTPUT_PATH)
