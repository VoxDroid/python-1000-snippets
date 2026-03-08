# sample3.py
# iterator that wraps another iterable to repeat each element twice

class DoubleIterator:
    def __init__(self, iterable):
        self._iter = iter(iterable)
        self._current = None
        self._count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._count == 0:
            self._current = next(self._iter)
            self._count = 2
        self._count -= 1
        return self._current

if __name__ == '__main__':
    for x in DoubleIterator([1, 2, 3]):
        print(x)
