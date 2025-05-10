# Metaclass

## Description
This snippet uses a metaclass to enforce a naming convention for class attributes.

## Code
```python
class NamingMeta(type):
    def __new__(cls, name, bases, attrs):
        for key in attrs:
            if not key.startswith("_") and not key[0].isupper():
                raise ValueError(f"Attribute '{key}' must start with uppercase")
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=NamingMeta):
    Name = "Test"
    Value = 42

print(MyClass.Name, MyClass.Value)
```

## Output
```
Test 42
```

## Explanation
- **Metaclass**: `NamingMeta` enforces that non-private attributes start with uppercase.
- **Logic**: Checks attribute names in `__new__` before class creation.
- **Complexity**: O(n) for n attributes during class creation.
- **Use Case**: Used for custom class creation or enforcing conventions.
- **Best Practice**: Use metaclasses sparingly; document their purpose clearly.