# sample3.py
# Use cProfile to dump stats to a file in temp.

import cProfile
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0501_profile.stats')


def compute_work(iterations=100000):
    s = 0
    for i in range(iterations):
        s += (i ^ (i << 1)) % 97
    return s


if __name__ == '__main__':
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    profiler = cProfile.Profile()
    profiler.enable()
    compute_work(100000)
    profiler.disable()
    profiler.dump_stats(OUTPUT_PATH)
    print('Wrote profiling stats to', OUTPUT_PATH)
