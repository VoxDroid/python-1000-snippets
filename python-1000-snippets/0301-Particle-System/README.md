# Particle System

## Description
This snippet demonstrates a simple particle system using `numpy`.

## Code
```python
import numpy as np
np.random.seed(42)
particles = np.random.random((10, 2))  # Positions
velocities = np.random.normal(0, 0.1, (10, 2))  # Velocities
particles += velocities  # Update positions
print("Updated Particle (first):", particles[0])
```

## Output
```
Updated Particle (first): [0.27325701 0.98213904]
```

## Explanation
- **Particle System**: Simulates particles with position and velocity updates.
- **Logic**: Updates particle positions based on random velocities.
- **Complexity**: O(n) for n particles.
- **Use Case**: Used for visual effects like smoke or fire.
- **Best Practice**: Add forces; handle lifetimes; optimize rendering.