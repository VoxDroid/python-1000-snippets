# sample3.py
# Use reduce to compute a cumulative result

from functools import reduce


def factorial(n):
    return reduce(lambda acc, x: acc * x, range(1, n + 1), 1)


def main():
    for n in (0, 1, 5, 7):
        print(f"{n}! = {factorial(n)}")


if __name__ == "__main__":
    main()
