# sample1.py
# Person class example (from README)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"

if __name__ == '__main__':
    p = Person('Bob', 25)
    print(p.introduce())
