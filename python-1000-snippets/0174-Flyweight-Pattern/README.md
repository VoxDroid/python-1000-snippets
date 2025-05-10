# Flyweight Pattern

## Description
This snippet implements the Flyweight pattern to share common state and reduce memory usage.

## Code
```python
class TreeType:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def render(self, x, y):
        return f"{self.name} tree at ({x}, {y}) in {self.color}"

class TreeFactory:
    _tree_types = {}
    @classmethod
    def get_tree_type(cls, name, color):
        key = (name, color)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color)
        return cls._tree_types[key]

tree = TreeFactory.get_tree_type("Oak", "Green")
print(tree.render(10, 20))
```

## Output
```
Oak tree at (10, 20) in Green
```

## Explanation
- **Flyweight Pattern**: `TreeFactory` reuses `TreeType` instances to share common state (`name`, `color`).
- **Logic**: Caches `TreeType` objects to minimize memory for repeated types.
- **Complexity**: O(1) for retrieval after caching.
- **Use Case**: Used in graphics or games with many similar objects.
- **Best Practice**: Separate intrinsic (shared) and extrinsic (unique) state; ensure thread-safety for factory.