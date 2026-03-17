# sample1.py
# Basic decorator stacking

import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Timing {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log
@timer
def greet(name):
    return f"Hello, {name}"


def main():
    print(greet("Alice"))


if __name__ == "__main__":
    main()
