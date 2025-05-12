# Dynamic Property Management

## Description
This snippet demonstrates dynamic property management with `property`.

## Code
```python
class Person:
    def __init__(self):
        self._name = "Alice"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

p = Person()
print(p.name)
p.name = "Bob"
print(p.name)
```

## Output
```
Alice
Bob
```

## Explanation
- **Dynamic Property Management**: Uses properties to control attribute access.
- **Logic**: Defines getter and setter for `name` using `property`.
- **Complexity**: O(1) for access.
- **Use Case**: Used for controlled attribute access in classes.
- **Best Practice**: Validate setters; use properties for encapsulation; document behavior.