# sample1.py
# Computed property example

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


def main():
    r = Rectangle(3, 4)
    print("area:", r.area)
    print("perimeter:", r.perimeter)


if __name__ == "__main__":
    main()
