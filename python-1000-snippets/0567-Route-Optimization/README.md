# Route Optimization

## Description
This snippet demonstrates route optimization using a greedy algorithm.

## Code
```python
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np
    distances = np.array([[0, 10, 15], [10, 0, 20], [15, 20, 0]])
    route = [0]
    visited = {0}
    for _ in range(2):
        last = route[-1]
        next_city = np.argmin([distances[last, i] if i not in visited else np.inf for i in range(3)])
        route.append(next_city)
        visited.add(next_city)
    print("Route:", route)
except ImportError:
    print("Mock Output: Route: [0, 1, 2]")
```

## Output
```
Mock Output: Route: [0, 1, 2]
```
*(Real output with `numpy`: `Route: [0, 1, 2]`)*

## Explanation
- **Route Optimization**: Finds shortest route visiting all cities.
- **Logic**: Uses a greedy nearest-neighbor algorithm.
- **Complexity**: O(n^2) for n cities.
- **Use Case**: Used in logistics for delivery routes.
- **Best Practice**: Use advanced solvers; account for constraints; validate routes.