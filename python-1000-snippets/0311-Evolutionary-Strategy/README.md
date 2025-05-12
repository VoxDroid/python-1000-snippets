# Evolutionary Strategy

## Description
This snippet demonstrates an evolutionary strategy to optimize a simple function using `numpy`.

## Code
```python
import numpy as np
np.random.seed(42)
population = np.random.random((10, 2))  # 10 individuals, 2D
fitness = np.sum(population, axis=1)  # Maximize sum
best_idx = np.argmax(fitness)
new_population = population + np.random.normal(0, 0.1, population.shape)
new_population[0] = population[best_idx]  # Keep best
print("Best Fitness:", fitness[best_idx])
```

## Output
```
Best Fitness: 1.3306524260084416
```

## Explanation
- **Evolutionary Strategy**: Optimizes a function by evolving a population with mutations.
- **Logic**: Evaluates fitness as the sum of coordinates, mutates population, and preserves the best.
- **Complexity**: O(n*d) for n individuals, d dimensions.
- **Use Case**: Used for continuous optimization problems like parameter tuning.
- **Best Practice**: Tune mutation rate; use recombination; balance exploration/exploitation.