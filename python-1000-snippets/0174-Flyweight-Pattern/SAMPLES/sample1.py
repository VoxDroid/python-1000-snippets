# sample1.py
# tree flyweight example (from README)

class TreeType:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def render(self, x, y):
        return f"{self.name} tree at ({x}, {y}) in {self.color}"

class TreeFactory:
    _tree_types = {}
    @classmethod
    def get_tree_type(cls, name, color):
        key = (name, color)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color)
        return cls._tree_types[key]

if __name__ == '__main__':
    t1 = TreeFactory.get_tree_type("Oak", "Green")
    t2 = TreeFactory.get_tree_type("Oak", "Green")
    print(t1 is t2)
    print(t1.render(10,20))
