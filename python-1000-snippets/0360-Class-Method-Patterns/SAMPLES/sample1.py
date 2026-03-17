# sample1.py
# Alternative constructor using classmethod

class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, string):
        return cls(string)


def main():
    p = Person.from_string("Alice")
    print(p.name)


if __name__ == "__main__":
    main()
