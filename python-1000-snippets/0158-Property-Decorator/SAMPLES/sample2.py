# sample2.py
# read-only computed property

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height

if __name__ == '__main__':
    r = Rectangle(3, 4)
    print('area', r.area)
    try:
        r.area = 20
    except AttributeError as e:
        print('cannot set read-only property', e)
