# Subsystem Facade

## Description
This snippet demonstrates the facade pattern to simplify subsystem interaction.

## Code
```python
class SubsystemA:
    def operation_a(self):
        return "Subsystem A"

class SubsystemB:
    def operation_b(self):
        return "Subsystem B"

class Facade:
    def __init__(self):
        self.sub_a = SubsystemA()
        self.sub_b = SubsystemB()
    
    def operation(self):
        return f"{self.sub_a.operation_a()} + {self.sub_b.operation_b()}"

facade = Facade()
print(facade.operation())
```

## Output
```
Subsystem A + Subsystem B
```

## Explanation
- **Subsystem Facade**: Simplifies access to complex subsystems.
- **Logic**: `Facade` coordinates calls to `SubsystemA` and `SubsystemB`.
- **Complexity**: O(1) per operation.
- **Use Case**: Used to provide a unified interface for APIs or libraries.
- **Best Practice**: Keep facade simple; avoid logic in facade; document subsystem interactions.