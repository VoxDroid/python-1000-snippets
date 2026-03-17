# sample1.py
# Metaclass that uppercases attribute names

class UpperCaseMeta(type):
    def __new__(cls, name, bases, attrs):
        upper_attrs = {k.upper(): v for k, v in attrs.items()}
        return super().__new__(cls, name, bases, upper_attrs)


class MyClass(metaclass=UpperCaseMeta):
    greeting = "hello"


def main():
    obj = MyClass()
    print(obj.GREETING)


if __name__ == "__main__":
    main()
