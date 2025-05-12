# Private Attribute Management

## Description
This snippet demonstrates managing private attributes with name mangling.

## Code
```python
class Person:
    def __init__(self):
        self.__secret = "Hidden"

    def get_secret(self):
        return self.__secret

p = Person()
print(p.get_secret())
```

## Output
```
Hidden
```

## Explanation
- **Private Attribute Management**: Uses double underscores for private attributes.
- **Logic**: Stores a secret and provides access via a getter.
- **Complexity**: O(1) for access.
- **Use Case**: Used for encapsulation in classes.
- **Best Practice**: Use properties for access; avoid direct mangled access; validate inputs.