# sample1.py
# Calculate the product of numbers using reduce

from functools import reduce

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    product = reduce(lambda x, y: x * y, nums)
    print('numbers:', nums)
    print('product:', product)
