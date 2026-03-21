# sample1.py
# Take a tracemalloc snapshot after creating sample objects.

import tracemalloc


def allocate_data(n):
    return [{'i': i, 'v': 'x' * 1024} for i in range(n)]


if __name__ == '__main__':
    tracemalloc.start()
    data = allocate_data(1000)
    snapshot = tracemalloc.take_snapshot()
    top = snapshot.statistics('filename')[:5]
    print('Top 5 allocations:')
    for stat in top:
        print(stat)
    del data
    tracemalloc.stop()
