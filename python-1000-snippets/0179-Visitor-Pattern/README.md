# Visitor Pattern

## Description
This snippet implements the Visitor pattern to separate algorithms from object structures.

## Code
```python
class Visitor:
    def visit_circle(self, circle):
        pass
    def visit_square(self, square):
        pass

class AreaCalculator(Visitor):
    def visit_circle(self, circle):
        return 3.14 * circle.radius ** 2
    def visit_square(self, square):
        return square.side ** 2

class Element:
    def accept(self, visitor):
        pass

class Circle(Element):
    def __init__(self, radius):
        self.radius = radius
    def accept(self, visitor):
        return visitor.visit_circle(self)

class Square(Element):
    def __init__(self, side):
        self.side = side
    def accept(self, visitor):
        return visitor.visit_square(self)

elements = [Circle(5), Square(4)]
visitor = AreaCalculator()
for elem in elements:
    print(f"Area: {elem.accept(visitor)}")
```

## Output
```
Area: 78.5
Area: 16
```

## Explanation
- **Visitor Pattern**: Separates `AreaCalculator` (algorithm) from `Circle` and `Square` (structure).
- **Logic**: `accept` calls the visitor’s specific method for each element type.
- **Complexity**: O(n) for n elements.
- **Use Case**: Used when operations vary by object type, like serialization.
- **Best Practice**: Minimize visitor interface changes; ensure stable element types.