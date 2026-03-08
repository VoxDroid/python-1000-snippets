# sample3.py
# Combine filter and map to process numbers

if __name__ == '__main__':
    nums = range(10)
    processed = list(map(lambda x: x*2, filter(lambda x: x%2, nums)))
    print('doubled odds:', processed)
