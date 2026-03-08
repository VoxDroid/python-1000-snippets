# 0101-Vector-Operations Cheatsheet

- **Addition/Subtraction**: element-wise; require same length.
- **Dot product**: `sum(v1[i]*v2[i] for i in range(n))`; gives scalar.
- **Norm**: Euclidean norm `sqrt(dot(v,v))`.
- **Cross product**: defined for 3D vectors: `(a2b3-a3b2, a3b1-a1b3, a1b2-a2b1)`.
- Use list comprehensions for concise implementation; use NumPy (`np.add`, `np.dot`, `np.cross`) for large data.
- Validate equal lengths and non-empty vectors.
