# sample3.py
# dynamic switching of renderer at runtime

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
    def set_renderer(self, renderer):
        self.renderer = renderer

class Circle(Shape):
    def draw(self):
        return self.renderer.render("Circle")

if __name__ == '__main__':
    c = Circle(VectorRenderer())
    print(c.draw())
    c.set_renderer(RasterRenderer())
    print(c.draw())
