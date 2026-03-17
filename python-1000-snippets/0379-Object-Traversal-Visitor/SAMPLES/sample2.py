# sample2.py
# Visitor traversing a simple tree structure

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def accept(self, visitor):
        visitor.visit(self)
        for child in self.children:
            child.accept(visitor)


class CollectValuesVisitor:
    def __init__(self):
        self.values = []

    def visit(self, node):
        self.values.append(node.value)


def main():
    tree = Node("root", [Node("a"), Node("b", [Node("b1"), Node("b2")])])
    visitor = CollectValuesVisitor()
    tree.accept(visitor)
    print(visitor.values)


if __name__ == "__main__":
    main()
