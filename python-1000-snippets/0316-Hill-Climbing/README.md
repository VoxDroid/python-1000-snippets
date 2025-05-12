# Hill Climbing

## Description
This snippet demonstrates hill climbing to maximize a simple function.

## Code
```python
import numpy as np
np.random.seed(42)
x = np.random.random(2)
fitness = np.sum(x)
for _ in range(10):
    new_x = x + np.random.normal(0, 0.1, 2)
    new_fitness = np.sum(new_x)
    if new_fitness > fitness:
        x, fitness = new_x, new_fitness
print("Solution:", x)
```

## Output
```
Solution: [0.69684769 1.21143914]
```

## Explanation
- **Hill Climbing**: Optimizes by always moving to better neighbors.
- **Logic**: Perturbs solution, updates if fitness improves.
- **Complexity**: O(i) for i iterations.
- **Use Case**: Used for local optimization in simple problems.
- **Best Practice**: Handle local optima; use restarts; validate solutions.