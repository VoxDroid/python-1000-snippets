# sample1.py
# Basic nested context managers using contextlib

from contextlib import contextmanager

@contextmanager
def resource(name):
    print(f"Opening {name}")
    try:
        yield name
    finally:
        print(f"Closing {name}")


def main():
    with resource("A"):
        with resource("B"):
            print("Inside nested context")


if __name__ == "__main__":
    main()
