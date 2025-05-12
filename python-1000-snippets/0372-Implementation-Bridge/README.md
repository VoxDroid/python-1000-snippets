# Implementation Bridge

## Description
This snippet demonstrates the bridge pattern to separate abstraction from implementation.

## Code
```python
class Implementor:
    def action(self):
        pass

class ConcreteImplementorA(Implementor):
    def action(self):
        return "Action A"

class Abstraction:
    def __init__(self, implementor):
        self.implementor = implementor
    
    def operation(self):
        return self.implementor.action()

bridge = Abstraction(ConcreteImplementorA())
print(bridge.operation())
```

## Output
```
Action A
```

## Explanation
- **Implementation Bridge**: Decouples abstraction from its implementation.
- **Logic**: `Abstraction` delegates to an `Implementor` instance.
- **Complexity**: O(1) per operation.
- **Use Case**: Used for platform-independent code or driver systems.
- **Best Practice**: Define clear interfaces; ensure extensibility; test implementations.