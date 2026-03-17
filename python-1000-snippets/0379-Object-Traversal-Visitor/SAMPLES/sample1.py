# sample1.py
# Basic visitor visiting a single element

class Visitor:
    def visit(self, element):
        raise NotImplementedError


class Element:
    def accept(self, visitor):
        raise NotImplementedError


class ConcreteElement(Element):
    def accept(self, visitor):
        visitor.visit(self)

    def operation(self):
        return "Element"


class ConcreteVisitor(Visitor):
    def visit(self, element):
        print(f"Visited: {element.operation()}")


def main():
    element = ConcreteElement()
    visitor = ConcreteVisitor()
    element.accept(visitor)


if __name__ == "__main__":
    main()
