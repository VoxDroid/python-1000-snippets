# Tree Structure Composite

## Description
This snippet demonstrates the composite pattern for a tree structure.

## Code
```python
class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def operation(self):
        return [child.operation() for child in self.children]

composite = Composite()
composite.add(Leaf())
composite.add(Leaf())
print(composite.operation())
```

## Output
```
['Leaf', 'Leaf']
```

## Explanation
- **Tree Structure Composite**: Treats individual and composite objects uniformly.
- **Logic**: `Composite` manages children and delegates operations.
- **Complexity**: O(n) for n children.
- **Use Case**: Used for hierarchical structures like file systems or UI components.
- **Best Practice**: Maintain consistent interfaces; manage child lifecycle; test traversal.