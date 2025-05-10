# Class Method

## Description
This snippet defines a class method to create an instance from a string.

## Code
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))

person = Person.from_string("Alice,25")
print(f"Name: {person.name}, Age: {person.age}")
```

## Output
```
Name: Alice, Age: 25
```

## Explanation
- **Class Method**: Uses `@classmethod` to define `from_string`, which takes `cls` and returns a new instance.
- **Logic**: Parses a string to create a `Person` object.
- **Complexity**: O(1) for parsing and instantiation.
- **Use Case**: Used for alternative constructors or factory methods.
- **Best Practice**: Use `cls` for flexibility with subclasses; validate input data.