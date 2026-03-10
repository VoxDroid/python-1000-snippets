# sample2.py
# another shape with raster renderer

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

class Rectangle(Shape):
    def draw(self):
        return self.renderer.render("Rectangle")

if __name__ == '__main__':
    rect = Rectangle(RasterRenderer())
    print(rect.draw())
