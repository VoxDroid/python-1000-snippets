# sample2.py
# decorator that preserves metadata using functools.wraps

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[log] calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    """add two numbers"""
    return a + b

if __name__ == '__main__':
    print(add(2, 3))
    print('name:', add.__name__)
    print('doc:', add.__doc__)

