# Ant Colony Optimization

## Description
This snippet demonstrates ant colony optimization (ACO) for a simple path-finding problem.

## Code
```python
import numpy as np
np.random.seed(42)
pheromones = np.ones((5, 5))  # 5 nodes
distances = np.random.random((5, 5))
np.fill_diagonal(distances, np.inf)
path = [0]
current = 0
for _ in range(3):
    probs = pheromones[current] / distances[current]
    probs /= probs.sum()
    current = np.random.choice(5, p=probs)
    path.append(current)
print("Path:", path)
```

## Output
```
Path: [0, 4, 1, 0]
```

## Explanation
- **Ant Colony Optimization**: Finds paths by simulating pheromone-based ant behavior.
- **Logic**: Selects next node based on pheromone and distance, builds a path.
- **Complexity**: O(n^2) for n nodes per ant.
- **Use Case**: Used for routing problems like TSP.
- **Best Practice**: Update pheromones; tune evaporation; handle large graphs.