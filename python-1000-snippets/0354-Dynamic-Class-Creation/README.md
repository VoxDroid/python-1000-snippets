# Dynamic Class Creation

## Description
This snippet demonstrates dynamic class creation using `type`.

## Code
```python
def method(self):
    return f"Hello, {self.name}"

DynamicClass = type("DynamicClass", (), {"name": "World", "greet": method})
obj = DynamicClass()
print(obj.greet())
```

## Output
```
Hello, World
```

## Explanation
- **Dynamic Class Creation**: Creates a class at runtime with attributes and methods.
- **Logic**: Uses `type` to define a class with a method and attribute.
- **Complexity**: O(1) for class creation.
- **Use Case**: Used in frameworks or for metaprogramming.
- **Best Practice**: Validate attributes; ensure method compatibility; avoid overuse.