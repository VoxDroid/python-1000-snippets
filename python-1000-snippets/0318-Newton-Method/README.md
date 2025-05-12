# Newton Method

## Description
This snippet demonstrates Newton’s method to find the root of a function.

## Code
```python
import numpy as np
x = 2.0
for _ in range(5):
    f = x**2 - 2  # f(x) = x^2 - 2
    df = 2 * x    # f'(x) = 2x
    x -= f / df
print("Root:", x)
```

## Output
```
Root: 1.4142135623730951
```

## Explanation
- **Newton Method**: Finds roots by iteratively using the tangent line.
- **Logic**: Solves x^2 - 2 = 0 to approximate sqrt(2).
- **Complexity**: O(i) for i iterations (converges quadratically).
- **Use Case**: Used for root-finding in numerical analysis.
- **Best Practice**: Handle division by zero; check convergence; validate initial guess.