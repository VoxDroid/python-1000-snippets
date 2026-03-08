# sample1.py
# compute squares in parallel

from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == '__main__':
    with Pool(2) as pool:
        nums = [1,2,3,4,5]
        print('Squares:', pool.map(square, nums))
