# Abstraction

## Description
This snippet demonstrates abstraction using an abstract base class to define a common interface.

## Code
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print("Area:", circle.area())
```

## Output
```
Area: 78.5
```

## Explanation
- **Abstraction**: `Shape` (abstract) defines an `area` method that subclasses like `Circle` must implement.
- **Logic**: `Circle` computes area as πr²; cannot instantiate `Shape`.
- **Complexity**: O(1) for area calculation.
- **Use Case**: Used to enforce interfaces in complex systems.
- **Best Practice**: Use `ABC` for abstract classes; document abstract methods clearly.