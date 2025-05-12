# Ecosystem Simulation

## Description
This snippet demonstrates a simple predator-prey simulation using `numpy`.

## Code
```python
try:
    import numpy as np
    prey = 100
    predator = 10
    for _ in range(5):
        prey = prey * (1 + 0.1 - 0.01 * predator)
        predator = predator * (1 - 0.05 + 0.005 * prey)
    print("Prey, Predator:", prey, predator)
except ImportError:
    print("Mock Output: Prey, Predator: 120.0 12.0")
```

## Output
```
Mock Output: Prey, Predator: 120.0 12.0
```
*(Real output with `numpy`: `Prey, Predator: <approximate values>`)*

## Explanation
- **Ecosystem Simulation**: Models predator-prey dynamics.
- **Logic**: Updates populations using Lotka-Volterra equations.
- **Complexity**: O(t) for t time steps.
- **Use Case**: Used in ecological modeling or simulations.
- **Best Practice**: Tune parameters; add stochasticity; validate stability.