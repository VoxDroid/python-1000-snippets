# sample2.py
# Create a class dynamically that inherits from a base class

class Base:
    def hello(self):
        return "base"


DynamicChild = type("DynamicChild", (Base,), {"hello": lambda self: "dynamic"})


def main():
    print(DynamicChild().hello())


if __name__ == "__main__":
    main()
