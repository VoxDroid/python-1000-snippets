# sample1.py
# Basic decorator pattern implementation

class Component:
    def operation(self):
        return "Base"


class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        return f"Decorated({self.component.operation()})"


def main():
    base = Component()
    decorated = Decorator(base)
    print(decorated.operation())


if __name__ == "__main__":
    main()
