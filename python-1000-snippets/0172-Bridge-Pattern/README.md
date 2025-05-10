# Bridge Pattern

## Description
This snippet implements the Bridge pattern to decouple an abstraction from its implementation.

## Code
```python
class Renderer:
    def render(self, shape):
        pass

class VectorRenderer(Renderer):
    def render(self, shape):
        return f"Rendering {shape} as vectors"

class RasterRenderer(Renderer):
    def render(self, shape):
        return f"Rendering {shape} as raster"

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return self.renderer.render("Circle")

circle = Circle(VectorRenderer())
print(circle.draw())
```

## Output
```
Rendering Circle as vectors
```

## Explanation
- **Bridge Pattern**: Separates `Shape` (abstraction) from `Renderer` (implementation).
- **Logic**: `Circle` uses a `Renderer` to draw, allowing different rendering methods.
- **Complexity**: O(1) for draw operation.
- **Use Case**: Used when abstractions and implementations vary independently.
- **Best Practice**: Define clear interfaces; ensure renderer compatibility.