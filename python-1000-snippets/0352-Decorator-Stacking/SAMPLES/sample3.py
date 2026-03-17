# sample3.py
# Decorator stacking with class-based decorators

from functools import wraps


class Counter:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log
@Counter
def say_hi():
    return "hi"


def main():
    print(say_hi())
    print(say_hi())
    print("call count:", say_hi.count)


if __name__ == "__main__":
    main()
