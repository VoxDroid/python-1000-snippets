# Matrix Multiplication

## Description
This snippet performs matrix multiplication on two matrices, ensuring compatibility of dimensions.

## Code
```python
def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    if cols_A != rows_B:
        return None
    result = [[0] * cols_B for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = matrix_multiply(A, B)
for row in result:
    print(row)
```

## Output
```
[19, 22]
[43, 50]
```

## Explanation
- **Matrix Multiplication**: Computes `C = A * B` where `C[i][j]` is the dot product of row `i` of `A` and column `j` of `B`.
- **Compatibility**: Requires `cols_A == rows_B`.
- **Complexity**: O(n * m * p) time for matrices of size n×m and m×p.
- **Use Case**: Used in graphics, machine learning, or network analysis.
- **Best Practice**: Validate dimensions; use NumPy for efficient large-scale multiplication.