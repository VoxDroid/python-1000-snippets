# sample2.py
# Named tuple for structured access

from collections import namedtuple


def main():
    Point = namedtuple("Point", ["x", "y"])
    p = Point(3, 4)
    print("point:", p)
    print("x:", p.x, "y:", p.y)


if __name__ == "__main__":
    main()
