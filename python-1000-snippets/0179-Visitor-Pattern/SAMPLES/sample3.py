# sample3.py
# perimeter calculator visitor

class Visitor:
    def visit_circle(self, circle):
        pass
    def visit_square(self, square):
        pass

class PerimeterCalculator(Visitor):
    def visit_circle(self, circle):
        return 2 * 3.14 * circle.radius
    def visit_square(self, square):
        return 4 * square.side

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
    shapes = [Circle(1), Square(2)]
    calc = PerimeterCalculator()
    for s in shapes:
        print('Perimeter:', s.accept(calc))
