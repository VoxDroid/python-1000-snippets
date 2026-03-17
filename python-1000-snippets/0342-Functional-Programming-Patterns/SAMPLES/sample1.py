# sample1.py
# Use functools.partial to create a fixed-parameter function

from functools import partial


def multiply(a, b):
    return a * b


def main():
    double = partial(multiply, 2)
    triple = partial(multiply, 3)

    values = [1, 2, 3, 4]
    print("values:", values)
    print("doubled:", list(map(double, values)))
    print("tripled:", list(map(triple, values)))


if __name__ == "__main__":
    main()
