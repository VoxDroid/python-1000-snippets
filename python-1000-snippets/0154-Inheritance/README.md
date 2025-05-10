# Inheritance

## Description
This snippet demonstrates inheritance by extending a `Person` class with a `Student` subclass.

## Code
```python
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

student = Student("Bob", "A")
print(student.introduce())
```

## Output
```
Name: Bob, Grade: A
```

## Explanation
- **Inheritance**: `Student` inherits from `Person`, adding a `grade` attribute and overriding `introduce`.
- **Logic**: Uses `super()` to call the parent’s `__init__` and `introduce`.
- **Complexity**: O(1) for initialization and method call.
- **Use Case**: Used to share code between related classes.
- **Best Practice**: Use `super()` for parent access; avoid deep inheritance hierarchies.