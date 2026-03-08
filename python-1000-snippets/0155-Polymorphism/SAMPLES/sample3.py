# sample3.py
# inheritance-based polymorphism

class Shape:
    def area(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    shapes = [Square(2), Circle(1)]
    for s in shapes:
        print('area', s.area())
