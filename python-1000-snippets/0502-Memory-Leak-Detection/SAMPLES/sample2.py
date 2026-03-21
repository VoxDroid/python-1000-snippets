# sample2.py
# Compare tracemalloc snapshots to detect memory growth.

import tracemalloc


def allocate_data(n):
    return [b'x'*1024 for _ in range(n)]


if __name__ == '__main__':
    tracemalloc.start()
    s1 = tracemalloc.take_snapshot()
    data = allocate_data(500)
    s2 = tracemalloc.take_snapshot()
    stats = s2.compare_to(s1, 'lineno')[:5]
    print('Top 5 offset allocations:')
    for stat in stats:
        print(stat)
    del data
    tracemalloc.stop()
