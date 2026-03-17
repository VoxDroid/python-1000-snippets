# sample2.py
# Decorator stacking can apply validation and logging

import functools


def validate_non_empty(func):
    @functools.wraps(func)
    def wrapper(s):
        if not s:
            raise ValueError("String must not be empty")
        return func(s)

    return wrapper


def log_call(func):
    @functools.wraps(func)
    def wrapper(s):
        print(f"Calling {func.__name__} with {s!r}")
        return func(s)

    return wrapper


@log_call
@validate_non_empty
def shout(s):
    return s.upper()


def main():
    print(shout("hello"))
    try:
        shout("")
    except ValueError as e:
        print("caught:", e)


if __name__ == "__main__":
    main()
