# Metaclass Customization

## Description
This snippet demonstrates a metaclass to enforce attribute naming.

## Code
```python
class UpperCaseMeta(type):
    def __new__(cls, name, bases, attrs):
        upper_attrs = {k.upper(): v for k, v in attrs.items()}
        return super().__new__(cls, name, bases, upper_attrs)

class MyClass(metaclass=UpperCaseMeta):
    greeting = "hello"

obj = MyClass()
print(obj.GREETING)
```

## Output
```
hello
```

## Explanation
- **Metaclass Customization**: Uses a metaclass to convert attribute names to uppercase.
- **Logic**: Modifies attributes during class creation.
- **Complexity**: O(n) for n attributes.
- **Use Case**: Used for advanced class customization in frameworks.
- **Best Practice**: Document metaclass behavior; avoid complexity; test thoroughly.