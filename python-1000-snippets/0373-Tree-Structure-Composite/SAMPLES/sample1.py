# sample1.py
# Simple composite with leaf nodes

class Component:
    def operation(self):
        raise NotImplementedError


class Leaf(Component):
    def operation(self):
        return "Leaf"


class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        return [child.operation() for child in self.children]


def main():
    composite = Composite()
    composite.add(Leaf())
    composite.add(Leaf())
    print(composite.operation())


if __name__ == "__main__":
    main()
