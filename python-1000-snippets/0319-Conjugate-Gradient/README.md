# Conjugate Gradient

## Description
This snippet demonstrates the conjugate gradient method for a linear system.

## Code
```python
import numpy as np
A = np.array([[4, 1], [1, 3]])  # Symmetric positive-definite
b = np.array([1, 2])
x = np.zeros(2)
r = b - A @ x
p = r.copy()
for _ in range(2):
    alpha = np.dot(r, r) / np.dot(p, A @ p)
    x += alpha * p
    r_new = r - alpha * A @ p
    beta = np.dot(r_new, r_new) / np.dot(r, r)
    p = r_new + beta * p
    r = r_new
print("Solution:", x)
```

## Output
```
Solution: [0.09090909 0.63636364]
```

## Explanation
- **Conjugate Gradient**: Solves Ax = b for a symmetric positive-definite matrix.
- **Logic**: Iteratively updates solution using conjugate directions.
- **Complexity**: O(n*k) for n dimensions, k iterations.
- **Use Case**: Used for large sparse linear systems.
- **Best Practice**: Precondition matrix; handle ill-conditioning; validate convergence.