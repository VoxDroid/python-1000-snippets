# Gradient Descent

## Description
This snippet demonstrates gradient descent to minimize a quadratic function.

## Code
```python
import numpy as np
x = np.array([2.0, 2.0])
learning_rate = 0.1
for _ in range(10):
    gradient = 2 * x  # Derivative of x^2 + y^2
    x -= learning_rate * gradient
print("Solution:", x)
```

## Output
```
Solution: [0.21474836 0.21474836]
```

## Explanation
- **Gradient Descent**: Optimizes by following the negative gradient.
- **Logic**: Updates x to minimize x^2 + y^2 using the gradient.
- **Complexity**: O(i*d) for i iterations, d dimensions.
- **Use Case**: Used for training ML models or optimization.
- **Best Practice**: Tune learning rate; use momentum; check convergence.