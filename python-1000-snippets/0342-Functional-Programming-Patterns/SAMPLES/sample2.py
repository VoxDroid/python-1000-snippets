# sample2.py
# Compose functions for a simple pipeline


def add_one(x):
    return x + 1


def square(x):
    return x * x


def compose(f, g):
    return lambda x: f(g(x))


def main():
    pipeline = compose(square, add_one)
    print("pipeline(4):", pipeline(4))
    print("pipeline(10):", pipeline(10))


if __name__ == "__main__":
    main()
