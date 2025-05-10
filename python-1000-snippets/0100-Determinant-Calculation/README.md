# Determinant Calculation

## Description
This snippet calculates the determinant of a square matrix using recursion for 2x2 and larger matrices.

## Code
```python
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        minor = [[matrix[i][k] for k in range(n) if k != j] for i in range(1, n)]
        det += ((-1) ** j) * matrix[0][j] * determinant(minor)
    
    return det

matrix = [[1, 2], [3, 4]]
print("Determinant:", determinant(matrix))
```

## Output
```
Determinant: -2
```

## Explanation
- **Determinant**: A scalar value computed recursively; for 2x2, it’s `ad - bc`.
- **Recursion**: For n×n matrices, uses the first row and computes minors.
- **Complexity**: O(n!) time due to recursive minor calculations.
- **Use Case**: Used in linear algebra, solving systems of equations, or computer graphics.
- **Best Practice**: Use LU decomposition or NumPy for large matrices; validate square matrices.