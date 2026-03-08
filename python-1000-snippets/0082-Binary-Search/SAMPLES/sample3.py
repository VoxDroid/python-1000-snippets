# sample3.py
# Using bisect module for insertion point

import bisect

if __name__ == '__main__':
    arr = [10,20,30,40]
    x = 25
    idx = bisect.bisect_left(arr, x)
    print(f'Insert {x} at index', idx)
    arr.insert(idx, x)
    print('new array', arr)
