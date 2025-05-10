# Class Definition

## Description
This snippet defines a simple `Person` class with attributes and a method to display information.

## Code
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"

person = Person("Alice", 30)
print(person.introduce())
```

## Output
```
Hi, I'm Alice, 30 years old
```

## Explanation
- **Class Definition**: Defines a `Person` class with `name` and `age` attributes and an `introduce` method.
- **Logic**: Stores data in instance variables; method returns a formatted string.
- **Complexity**: O(1) for initialization and method call.
- **Use Case**: Used for modeling real-world entities in OOP.
- **Best Practice**: Initialize attributes in `__init__`; use clear method names.