# sample3.py
# Pipeline using filter/map/reduce with lambdas

from functools import reduce


def sum_of_squares_of_evens(numbers):
    evens = filter(lambda x: x % 2 == 0, numbers)
    squares = map(lambda x: x * x, evens)
    return reduce(lambda a, b: a + b, squares, 0)


def main():
    values = list(range(1, 11))
    print("values:", values)
    print("sum of squares of evens:", sum_of_squares_of_evens(values))


if __name__ == "__main__":
    main()
