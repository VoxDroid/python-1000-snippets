# sample1.py
# example using classmethod as an alternative constructor

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))

if __name__ == '__main__':
    person = Person.from_string("Alice,25")
    print(f"Name: {person.name}, Age: {person.age}")
