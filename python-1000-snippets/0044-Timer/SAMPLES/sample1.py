# sample1.py
# Measure time taken by a simple loop

import time

if __name__ == '__main__':
    start = time.time()
    total = 0
    for i in range(1000000):
        total += i
    end = time.time()
    print('result:', total)
    print('elapsed (time.time):', end - start)
