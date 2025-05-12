# Object Traversal Visitor

## Description
This snippet demonstrates the visitor pattern for object traversal.

## Code
```python
class Visitor:
    def visit(self, element):
        pass

class Element:
    def accept(self, visitor):
        pass

class ConcreteElement(Element):
    def accept(self, visitor):
        visitor.visit(self)
    
    def operation(self):
        return "Element"

class ConcreteVisitor(Visitor):
    def visit(self, element):
        print(f"Visited: {element.operation()}")

element = ConcreteElement()
visitor = ConcreteVisitor()
element.accept(visitor)
```

## Output
```
Visited: Element
```

## Explanation
- **Object Traversal Visitor**: Separates operations from object structure.
- **Logic**: `Element` accepts a `Visitor` that performs an operation.
- **Complexity**: O(1) per visit.
- **Use Case**: Used for AST traversal or report generation.
- **Best Practice**: Define clear visitor interface; avoid modifying structure; test visitors.