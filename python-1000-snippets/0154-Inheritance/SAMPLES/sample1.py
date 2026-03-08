# sample1.py
# simple Person/Student inheritance example

class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        return f"Name: {self.name}"

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
    def introduce(self):
        return f"{super().introduce()}, Grade: {self.grade}"

if __name__ == '__main__':
    s = Student('Carol', 'B')
    print(s.introduce())
