# sample3.py
# Demonstrate relative imports when organized into a package

# This requires running from the package root.
from utils import double


def main():
    print("double(5):", double(5))


if __name__ == "__main__":
    main()
