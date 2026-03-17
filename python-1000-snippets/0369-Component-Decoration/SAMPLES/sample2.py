# sample2.py
# Stack multiple decorators to modify behavior

class Component:
    def operation(self):
        return "Base"


class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        return self.component.operation()


class UppercaseDecorator(Decorator):
    def operation(self):
        return self.component.operation().upper()


class BracketDecorator(Decorator):
    def operation(self):
        return f"[{self.component.operation()}]"


def main():
    base = Component()
    decorated = BracketDecorator(UppercaseDecorator(base))
    print(decorated.operation())


if __name__ == "__main__":
    main()
