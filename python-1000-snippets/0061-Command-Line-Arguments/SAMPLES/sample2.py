# sample2.py
# Sum integer arguments passed on the command line

import sys

if __name__ == '__main__':
    nums = [int(x) for x in sys.argv[1:]]
    print('numbers:', nums)
    print('sum =', sum(nums))
