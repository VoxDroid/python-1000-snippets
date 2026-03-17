# sample3.py
# Composite that aggregates values from leaf nodes

class Component:
    def value(self):
        raise NotImplementedError


class Leaf(Component):
    def __init__(self, val):
        self._val = val

    def value(self):
        return self._val


class Node(Component):
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)

    def value(self):
        return sum(child.value() for child in self.children)


def main():
    root = Node()
    root.add(Leaf(1))
    root.add(Leaf(2))
    child = Node()
    child.add(Leaf(3))
    root.add(child)
    print("total:", root.value())


if __name__ == "__main__":
    main()
