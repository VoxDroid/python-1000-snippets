# sample1.py
# timing decorator from README

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper

@timing_decorator
def slow(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print('Result:', slow(0.5))
