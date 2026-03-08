# sample2.py
# Sum numbers with initializer using reduce

from functools import reduce

if __name__ == '__main__':
    nums = [10, 20, 30]
    total = reduce(lambda a, b: a + b, nums, 100)
    print('nums:', nums)
    print('total with initial 100:', total)
