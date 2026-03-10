# sample3.py
# dynamic traversal and removal

class Component:
    def operation(self):
        pass

class Leaf(Component):
    def __init__(self, value):
        self.value = value
    def operation(self):
        return str(self.value)

class Composite(Component):
    def __init__(self):
        self.children = []
    def add(self, comp):
        self.children.append(comp)
    def remove(self, comp):
        self.children.remove(comp)
    def operation(self):
        return ''.join(child.operation() for child in self.children)

if __name__ == '__main__':
    comp = Composite()
    l1 = Leaf(1)
    l2 = Leaf(2)
    comp.add(l1)
    comp.add(l2)
    print('before', comp.operation())
    comp.remove(l1)
    print('after', comp.operation())
