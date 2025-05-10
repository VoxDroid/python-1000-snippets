# Composite Pattern

## Description
This snippet implements the Composite pattern to treat individual and composite objects uniformly.

## Code
```python
class Component:
    def operation(self):
        pass

class Leaf(Component):
    def __init__(self, name):
        self.name = name
    def operation(self):
        return f"Leaf {self.name}"

class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []
    def add(self, component):
        self.children.append(component)
    def operation(self):
        results = [child.operation() for child in self.children]
        return f"Composite {self.name}: [{', '.join(results)}]"

composite = Composite("A")
composite.add(Leaf("B"))
composite.add(Leaf("C"))
print(composite.operation())
```

## Output
```
Composite A: [Leaf B, Leaf C]
```

## Explanation
- **Composite Pattern**: `Composite` and `Leaf` share a `Component` interface, allowing recursive structures.
- **Logic**: `Composite` aggregates `Leaf` objects and combines their operations.
- **Complexity**: O(n) for n children in operation.
- **Use Case**: Used for tree-like structures, like file systems or UI components.
- **Best Practice**: Ensure consistent interfaces; manage child additions carefully.