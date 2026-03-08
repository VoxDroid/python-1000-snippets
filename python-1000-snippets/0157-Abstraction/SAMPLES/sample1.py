# sample1.py
# basic abstract base class example (from README)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

if __name__ == '__main__':
    circle = Circle(5)
    print('Area:', circle.area())
