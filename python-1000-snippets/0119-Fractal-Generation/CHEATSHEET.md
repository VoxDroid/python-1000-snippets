# 0119-Fractal-Generation Cheatsheet

- **Purpose**: recursively build a text‑based Sierpinski triangle.
- **Function**: `sierpinski_triangle(n)` returns list of strings, depth `n`.

```python
from fractal_generation import sierpinski_triangle

for row in sierpinski_triangle(3):
    print(row)
```

- Complexity grows exponentially with depth (≈2^n lines).
- Useful for demonstrating recursion or simple fractal geometry.
- Can be extended to graphics by plotting '*' positions.

