# Simulated Annealing

## Description
This snippet demonstrates simulated annealing to maximize a simple function.

## Code
```python
import numpy as np
np.random.seed(42)
x = np.random.random(2)
fitness = np.sum(x)
T = 1.0
for _ in range(10):
    new_x = x + np.random.normal(0, 0.1, 2)
    new_fitness = np.sum(new_x)
    if new_fitness > fitness or np.random.random() < np.exp((new_fitness - fitness) / T):
        x, fitness = new_x, new_fitness
    T *= 0.9
print("Solution:", x)
```

## Output
```
Solution: [0.22333713 0.80880044]
```

## Explanation
- **Simulated Annealing**: Optimizes by accepting worse solutions with decreasing probability.
- **Logic**: Perturbs solution, accepts based on fitness and temperature.
- **Complexity**: O(i) for i iterations.
- **Use Case**: Used for combinatorial optimization like scheduling.
- **Best Practice**: Tune cooling schedule; balance exploration; validate convergence.