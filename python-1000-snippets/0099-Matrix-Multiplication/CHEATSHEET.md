# 0099-Matrix-Multiplication Cheatsheet

- Multiply A (n×m) by B (m×p) to get C (n×p).
- Ensure number of columns in A equals number of rows in B; otherwise return `None` or raise error.
- Standard triple-loop implementation:
  ```python
  for i in range(n):
      for j in range(p):
          for k in range(m):
              C[i][j] += A[i][k] * B[k][j]
  ```
- Complexity O(n·m·p). For better performance, use libraries (NumPy) with optimized BLAS.
- Check matrix dimensions before loop, and consider special cases (identity, sparse matrices).
- Python lists are fine for small matrices; avoid extremely large sizes without numpy.
