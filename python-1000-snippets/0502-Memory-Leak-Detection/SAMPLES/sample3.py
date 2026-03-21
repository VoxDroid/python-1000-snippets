# sample3.py
# Write snapshot top entries to temp/0502_mem_snapshot.txt

import os
import tracemalloc

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0502_mem_snapshot.txt')


def allocate_data(n):
    return [{'i': i, 'strings': ['x'*2048 for _ in range(5)]} for i in range(n)]


if __name__ == '__main__':
    tracemalloc.start()
    data = allocate_data(200)
    snapshot = tracemalloc.take_snapshot()
    top = snapshot.statistics('lineno')[:5]
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write('Top 5 allocations:\n')
        for stat in top:
            f.write(str(stat) + '\n')
    print('Wrote memory snapshot to', OUTPUT_PATH)
    del data
    tracemalloc.stop()
