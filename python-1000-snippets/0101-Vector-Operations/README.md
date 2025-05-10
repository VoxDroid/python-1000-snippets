# Vector Operations

## Description
This snippet performs basic vector operations: addition, subtraction, and dot product.

## Code
```python
def vector_add(v1, v2):
    if len(v1) != len(v2):
        return None
    return [v1[i] + v2[i] for i in range(len(v1))]

def vector_subtract(v1, v2):
    if len(v1) != len(v2):
        return None
    return [v1[i] - v2[i] for i in range(len(v1))]

def dot_product(v1, v2):
    if len(v1) != len(v2):
        return None
    return sum(v1[i] * v2[i] for i in range(len(v1)))

v1 = [1, 2, 3]
v2 = [4, 5, 6]
print("Addition:", vector_add(v1, v2))
print("Subtraction:", vector_subtract(v1, v2))
print("Dot Product:", dot_product(v1, v2))
```

## Output
```
Addition: [5, 7, 9]
Subtraction: [-3, -3, -3]
Dot Product: 32
```

## Explanation
- **Vector Operations**:
  - Addition: Element-wise sum.
  - Subtraction: Element-wise difference.
  - Dot Product: Sum of element-wise products.
- **Validation**: Checks for equal vector lengths.
- **Complexity**: O(n) time for each operation.
- **Use Case**: Used in physics, machine learning, or graphics.
- **Best Practice**: Use NumPy for efficiency; add more operations like cross product.