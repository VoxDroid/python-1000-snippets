# sample2.py
# demonstrate subclassing and cls pointing to subclass

class Base:
    def __init__(self, x):
        self.x = x
    @classmethod
    def create(cls, x):
        return cls(x)

class Sub(Base):
    pass

if __name__ == '__main__':
    b = Base.create(5)
    s = Sub.create(10)
    print(type(b), b.x)
    print(type(s), s.x)
