# sample3.py
# cached property using property and internal variable

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None
    @property
    def area(self):
        if self._area is None:
            self._area = 3.14 * self.radius ** 2
        return self._area

if __name__ == '__main__':
    c = Circle(2)
    print('first read', c.area)
    print('second read (cached)', c.area)
