# sample1.py
# basic bridge example from README

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

if __name__ == '__main__':
    circle = Circle(VectorRenderer())
    print(circle.draw())
