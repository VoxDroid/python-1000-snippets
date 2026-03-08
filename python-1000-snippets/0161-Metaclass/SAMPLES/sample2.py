# sample2.py
# register subclasses automatically

registry = {}

class RegisterMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        registry[name] = cls

class Base(metaclass=RegisterMeta):
    pass

class Child(Base):
    pass

if __name__ == '__main__':
    print('registry', registry)    
