# sample2.py
# registry-based factory to avoid if/elif chain

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return 'circle'

class Square(Shape):
    def draw(self):
        return 'square'

class ShapeFactory:
    _creators = {}
    @classmethod
    def register(cls, name, creator):
        cls._creators[name] = creator
    @classmethod
    def create(cls, name):
        if name not in cls._creators:
            raise ValueError('Unknown shape')
        return cls._creators[name]()

# register types
ShapeFactory.register('circle', Circle)
ShapeFactory.register('square', Square)

if __name__ == '__main__':
    print(ShapeFactory.create('circle').draw())
    print(ShapeFactory.create('square').draw())
