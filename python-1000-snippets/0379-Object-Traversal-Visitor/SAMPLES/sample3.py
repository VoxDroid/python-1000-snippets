# sample3.py
# Visiting different node types with a single visitor

class Node:
    def accept(self, visitor):
        raise NotImplementedError


class TextNode(Node):
    def __init__(self, text):
        self.text = text

    def accept(self, visitor):
        visitor.visit_text(self)


class ImageNode(Node):
    def __init__(self, url):
        self.url = url

    def accept(self, visitor):
        visitor.visit_image(self)


class RenderVisitor:
    def visit_text(self, node):
        print(f"Render text: {node.text}")

    def visit_image(self, node):
        print(f"Render image: {node.url}")


def main():
    nodes = [TextNode("hello"), ImageNode("img.png"), TextNode("world")]
    visitor = RenderVisitor()
    for n in nodes:
        n.accept(visitor)


if __name__ == "__main__":
    main()
