# Component Decoration

## Description
This snippet demonstrates the decorator pattern for adding behavior.

## Code
```python
class Component:
    def operation(self):
        return "Base"

class Decorator(Component):
    def __init__(self, component):
        self.component = component
    
    def operation(self):
        return f"Decorated({self.component.operation()})"

base = Component()
decorated = Decorator(base)
print(decorated.operation())
```

## Output
```
Decorated(Base)
```

## Explanation
- **Component Decoration**: Adds behavior without modifying the base component.
- **Logic**: Wraps a component to extend its `operation`.
- **Complexity**: O(1) per call.
- **Use Case**: Used for flexible feature addition like logging or formatting.
- **Best Practice**: Maintain interface; allow multiple decorators; test composition.