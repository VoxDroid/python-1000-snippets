# sample1.py
# area calculator visitor (from README)

class Visitor:
    def visit_circle(self, circle):
        pass
    def visit_square(self, square):
        pass

class AreaCalculator(Visitor):
    def visit_circle(self, circle):
        return 3.14 * circle.radius ** 2
    def visit_square(self, square):
        return square.side ** 2

class Element:
    def accept(self, visitor):
        pass

class Circle(Element):
    def __init__(self, radius):
        self.radius = radius
    def accept(self, visitor):
        return visitor.visit_circle(self)

class Square(Element):
    def __init__(self, side):
        self.side = side
    def accept(self, visitor):
        return visitor.visit_square(self)

if __name__ == '__main__':
    elements = [Circle(5), Square(4)]
    visitor = AreaCalculator()
    for elem in elements:
        print(f"Area: {elem.accept(visitor)}")
