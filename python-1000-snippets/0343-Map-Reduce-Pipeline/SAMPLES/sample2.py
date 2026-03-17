# sample2.py
# Generator pipeline: filter, map, reduce

from functools import reduce


def sum_of_squares_of_odds(numbers):
    odds = (n for n in numbers if n % 2 != 0)
    squares = (n * n for n in odds)
    return reduce(lambda a, b: a + b, squares, 0)


def main():
    numbers = list(range(1, 11))
    print("numbers:", numbers)
    print("sum of squares of odd numbers:", sum_of_squares_of_odds(numbers))


if __name__ == "__main__":
    main()
