# sample3.py
# Use __slots__ to restrict attributes and reduce memory

class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    p = Point(1, 2)
    print("Point:", p.x, p.y)
    try:
        p.z = 3
    except AttributeError as e:
        print("cannot set attribute:", e)


if __name__ == "__main__":
    main()
