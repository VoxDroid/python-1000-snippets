# 0100-Determinant-Calculation Cheatsheet

- Determinant defined for square matrices; scalar value capturing scale factor and orientation.
- For 1×1: element itself; for 2×2: `a*d - b*c`.
- Recursive expansion along first row (Laplace expansion):
  ```python
  det = sum((-1)**j * matrix[0][j] * determinant(minor(matrix,0,j)) for j in range(n))
  ```
- Minor is matrix removing row 0 and column j.
- Computational cost grows factorially; use optimized algorithms (LU decomposition) or libraries (`numpy.linalg.det`).
- Determinant zero indicates singular (non-invertible) matrix.
- Useful for Cramer’s rule, change of variables, geometry.
