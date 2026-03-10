# sample2.py
# name printer visitor

class Visitor:
    def visit_circle(self, circle):
        pass
    def visit_square(self, square):
        pass

class NamePrinter(Visitor):
    def visit_circle(self, circle):
        return f"Circle(radius={circle.radius})"
    def visit_square(self, square):
        return f"Square(side={square.side})"

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
    elements = [Circle(2), Square(3)]
    printer = NamePrinter()
    for e in elements:
        print(e.accept(printer))
