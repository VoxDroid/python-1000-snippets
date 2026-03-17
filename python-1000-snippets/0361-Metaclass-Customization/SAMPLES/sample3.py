# sample3.py
# Metaclass enforcing uppercase class attribute names and raising on violation

class UpperAttrMeta(type):
    def __new__(cls, name, bases, attrs):
        for k in attrs:
            if not k.startswith("__") and not k.isupper():
                raise TypeError("Attributes must be uppercase")
        return super().__new__(cls, name, bases, attrs)


class Good(metaclass=UpperAttrMeta):
    VALUE = 42


def main():
    print("Good.VALUE:", Good.VALUE)
    try:
        class Bad(metaclass=UpperAttrMeta):
            value = 1
    except TypeError as e:
        print("caught error:", e)


if __name__ == "__main__":
    main()
