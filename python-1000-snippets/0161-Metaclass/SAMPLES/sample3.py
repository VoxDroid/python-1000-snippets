# sample3.py
# add method automatically via metaclass

class AddMethodMeta(type):
    def __new__(cls, name, bases, attrs):
        def greet(self):
            return f"hello from {name}"
        attrs['greet'] = greet
        return super().__new__(cls, name, bases, attrs)

class Person(metaclass=AddMethodMeta):
    pass

if __name__ == '__main__':
    p = Person()
    print(p.greet())
