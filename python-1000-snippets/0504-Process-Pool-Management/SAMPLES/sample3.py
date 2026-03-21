# sample3.py
# Save process pool results to temp file.

import os
from concurrent.futures import ProcessPoolExecutor

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0504_process_pool.txt')


def cube(n):
    return n**3


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(cube, range(1, 21)))

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write('Cubes count: ' + str(len(results)) + '\n')
        f.write('Sum cubes: ' + str(sum(results)) + '\n')

    print('Wrote process pool stats to', OUTPUT_PATH)
