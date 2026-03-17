# sample2.py
# Property with validation

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value


def main():
    p = Person("Alice")
    print(p.name)
    p.name = "Bob"
    print(p.name)
    try:
        p.name = ""
    except ValueError as e:
        print("error:", e)


if __name__ == "__main__":
    main()
