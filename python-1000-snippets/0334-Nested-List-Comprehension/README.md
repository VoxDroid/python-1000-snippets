# Nested List Comprehension

## Description
This snippet demonstrates nested list comprehension to create a matrix.

## Code
```python
rows, cols = 3, 4
matrix = [[i * cols + j for j in range(cols)] for i in range(rows)]
print("Matrix:", matrix)
```

## Output
```
Matrix: [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
```

## Explanation
- **Nested List Comprehension**: Creates a 3x4 matrix with sequential values.
- **Logic**: Uses nested loops within a comprehension to populate rows and columns.
- **Complexity**: O(r*c) for r rows, c columns.
- **Use Case**: Used for concise matrix initialization or data transformation.
- **Best Practice**: Ensure readability; avoid excessive nesting; validate dimensions.