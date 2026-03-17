# sample1.py
# Demonstrate name mangling for pseudo-private attributes

class Person:
    def __init__(self, secret):
        self.__secret = secret

    def get_secret(self):
        return self.__secret


def main():
    p = Person("hidden")
    print("get_secret():", p.get_secret())
    # Accessing the mangled attribute (not recommended):
    print("mangled access:", p._Person__secret)


if __name__ == "__main__":
    main()
