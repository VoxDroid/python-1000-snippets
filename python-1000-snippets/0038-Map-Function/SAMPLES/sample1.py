# sample1.py
# Square numbers using map and lambda

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    squares = map(lambda x: x**2, nums)
    print('original:', nums)
    print('squares:', list(squares))
