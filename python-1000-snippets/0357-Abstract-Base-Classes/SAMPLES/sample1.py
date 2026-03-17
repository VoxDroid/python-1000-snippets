# sample1.py
# Abstract base class enforcing an interface

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


def main():
    s = Square(3)
    print("area:", s.area())


if __name__ == "__main__":
    main()
