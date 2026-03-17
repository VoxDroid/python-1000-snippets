# sample3.py
# Dynamically add methods to a class at runtime

class Base:
    def greet(self):
        return "hi"


def add_method(cls, name, func):
    setattr(cls, name, func)


def main():
    add_method(Base, "shout", lambda self: self.greet().upper())
    b = Base()
    print(b.greet())
    print(b.shout())


if __name__ == "__main__":
    main()
