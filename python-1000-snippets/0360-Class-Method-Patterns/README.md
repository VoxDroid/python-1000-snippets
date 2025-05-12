# Class Method Patterns

## Description
This snippet demonstrates class methods for alternative constructors.

## Code
```python
class Person:
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def from_string(cls, string):
        return cls(string)

p = Person.from_string("Alice")
print(p.name)
```

## Output
```
Alice
```

## Explanation
- **Class Method Patterns**: Uses `@classmethod` for alternative instantiation.
- **Logic**: Creates a `Person` instance from a string.
- **Complexity**: O(1) per call.
- **Use Case**: Used for factory-like creation or class-level operations.
- **Best Practice**: Use `cls` for flexibility; document purpose; validate inputs.