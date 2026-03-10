# sample2.py
# shallow vs deep copy demonstration

import copy

class Data:
    def __init__(self, items):
        self.items = items
    def clone_shallow(self):
        return copy.copy(self)
    def clone_deep(self):
        return copy.deepcopy(self)

if __name__ == '__main__':
    d = Data([1, 2])
    ds = d.clone_shallow()
    dd = d.clone_deep()
    ds.items.append(3)
    print('original', d.items)
    print('shallow', ds.items)
    print('deep', dd.items)