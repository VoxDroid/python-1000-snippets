# sample3.py
# Custom map and reduce utility functions

from functools import reduce


def my_map(fn, iterable):
    for x in iterable:
        yield fn(x)


def my_reduce(fn, iterable, start=None):
    iterator = iter(iterable)
    if start is None:
        try:
            start = next(iterator)
        except StopIteration:
            raise TypeError("my_reduce() of empty sequence with no initial value")
    return reduce(fn, iterator, start)


def main():
    data = [1, 2, 3, 4]
    print("data:", data)
    doubled = list(my_map(lambda x: x * 2, data))
    print("doubled:", doubled)
    total = my_reduce(lambda a, b: a + b, data)
    print("sum:", total)


if __name__ == "__main__":
    main()
