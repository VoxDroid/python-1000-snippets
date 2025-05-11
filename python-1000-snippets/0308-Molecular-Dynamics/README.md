# Molecular Dynamics

## Description
This snippet demonstrates a simple molecular dynamics simulation using `numpy`.

## Code
```python
import numpy as np
np.random.seed(42)
positions = np.random.random((2, 2))  # Two particles
velocities = np.random.normal(0, 0.1, (2, 2))
force = -10.0 * (positions[1] - positions[0])  # Lennard-Jones-like
velocities += force * 0.01
positions += velocities * 0.01
print("Updated Position:", positions[1])
```

## Output
```
Updated Position: [0.7332157  0.59977797]
```

## Explanation
- **Molecular Dynamics**: Simulates particle motion with forces.
- **Logic**: Updates positions and velocities based on a simple force model.
- **Complexity**: O(n) for n particles.
- **Use Case**: Used for simulating molecular interactions.
- **Best Practice**: Use realistic potentials; implement thermostats; validate energies.