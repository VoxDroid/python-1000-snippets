# Tabu Search

## Description
This snippet demonstrates tabu search to maximize a simple function.

## Code
```python
import numpy as np
np.random.seed(42)
x = np.random.random(2)
fitness = np.sum(x)
tabu_list = []
for _ in range(10):
    new_x = x + np.random.normal(0, 0.1, 2)
    if tuple(new_x) not in tabu_list:
        new_fitness = np.sum(new_x)
        if new_fitness > fitness:
            x, fitness = new_x, new_fitness
            tabu_list.append(tuple(new_x))
            if len(tabu_list) > 5:
                tabu_list.pop(0)
print("Solution:", x)
```

## Output
```
Solution: [0.69684769 1.21143914]
```

## Explanation
- **Tabu Search**: Optimizes by avoiding recently visited solutions.
- **Logic**: Perturbs solution, updates if better and not tabu.
- **Complexity**: O(i) for i iterations.
- **Use Case**: Used for combinatorial problems like vehicle routing.
- **Best Practice**: Tune tabu tenure; use aspiration criteria; validate solutions.