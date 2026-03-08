# sample2.py
# Compare time.time() and time.perf_counter()

import time

if __name__ == '__main__':
    start1 = time.time()
    start2 = time.perf_counter()
    for i in range(1000000):
        pass
    end1 = time.time()
    end2 = time.perf_counter()
    print('time.time elapsed:', end1 - start1)
    print('perf_counter elapsed:', end2 - start2)
