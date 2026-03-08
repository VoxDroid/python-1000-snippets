# sample3.py
# Chain map and filter to process numbers

if __name__ == '__main__':
    nums = range(10)
    evens = filter(lambda x: x%2==0, nums)
    doubled = map(lambda x: x*2, evens)
    print('doubled evens:', list(doubled))
