# sample1.py
# Import and use utility functions from a separate module

from utils import double, triple


def main():
    print("double(3):", double(3))
    print("triple(3):", triple(3))


if __name__ == "__main__":
    main()
