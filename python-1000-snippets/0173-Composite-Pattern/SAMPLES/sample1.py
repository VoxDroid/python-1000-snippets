# sample1.py
# basic composite example (from README)

class Component:
    def operation(self):
        pass

class Leaf(Component):
    def __init__(self, name):
        self.name = name
    def operation(self):
        return f"Leaf {self.name}"

class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []
    def add(self, component):
        self.children.append(component)
    def operation(self):
        results = [child.operation() for child in self.children]
        return f"Composite {self.name}: [{', '.join(results)}]"

if __name__ == '__main__':
    composite = Composite("A")
    composite.add(Leaf("B"))
    composite.add(Leaf("C"))
    print(composite.operation())
