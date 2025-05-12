# Complex Object Builder

## Description
This snippet demonstrates the builder pattern for complex object construction.

## Code
```python
class Product:
    def __init__(self):
        self.parts = []
    
    def add(self, part):
        self.parts.append(part)

class Builder:
    def __init__(self):
        self.product = Product()
    
    def build_part_a(self):
        self.product.add("Part A")
        return self
    
    def build_part_b(self):
        self.product.add("Part B")
        return self
    
    def get_product(self):
        return self.product

builder = Builder()
product = builder.build_part_a().build_part_b().get_product()
print(product.parts)
```

## Output
```
['Part A', 'Part B']
```

## Explanation
- **Complex Object Builder**: Constructs objects step-by-step.
- **Logic**: `Builder` adds parts to a `Product` with a fluent interface.
- **Complexity**: O(n) for n parts.
- **Use Case**: Used for constructing complex objects like configurations or documents.
- **Best Practice**: Ensure valid construction; support optional parts; test builder.