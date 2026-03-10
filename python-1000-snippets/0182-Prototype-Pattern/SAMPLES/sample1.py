# sample1.py
# prototype clone demonstrating deep copy

import copy

class Prototype:
    def __init__(self, field):
        self.field = field
    def clone(self):
        return copy.deepcopy(self)

if __name__ == '__main__':
    p1 = Prototype([1, 2, 3])
    p2 = p1.clone()
    p2.field.append(4)
    print('p1', p1.field)
    print('p2', p2.field)