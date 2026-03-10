# sample3.py
# registry of prototypes to clone from

class PrototypeRegistry:
    def __init__(self):
        self._prototypes = {}
    def register(self, name, prototype):
        self._prototypes[name] = prototype
    def clone(self, name):
        import copy
        return copy.deepcopy(self._prototypes[name])

class Widget:
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return f"Widget({self.color})"

if __name__ == '__main__':
    reg = PrototypeRegistry()
    reg.register('red', Widget('red'))
    w1 = reg.clone('red')
    w2 = reg.clone('red')
    print(w1, w2, 'same?', w1 is w2)