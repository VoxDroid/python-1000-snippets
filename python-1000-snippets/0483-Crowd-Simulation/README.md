# Crowd Simulation

## Description
This snippet demonstrates a simple crowd simulation using `numpy`.

## Code
```python
try:
    import numpy as np
    agents = np.random.rand(10, 2) * 10
    for _ in range(5):
        agents += np.random.randn(10, 2) * 0.1
    print("Agent positions:\n", agents[:2])
except ImportError:
    print("Mock Output: Agent positions: [[5.1 5.2] [3.3 3.4]]")
```

## Output
```
Mock Output: Agent positions: [[5.1 5.2] [3.3 3.4]]
```
*(Real output with `numpy`: `Agent positions: <random 2D positions>`)*

## Explanation
- **Crowd Simulation**: Simulates agent movement with random walks.
- **Logic**: Updates agent positions with small random steps.
- **Complexity**: O(n * t) for n agents, t steps.
- **Use Case**: Used in games or urban planning simulations.
- **Best Practice**: Add collision avoidance; model behaviors; visualize movement.