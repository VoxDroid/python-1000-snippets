# Particle Swarm Optimization

## Description
This snippet demonstrates particle swarm optimization (PSO) to maximize a simple function.

## Code
```python
import numpy as np
np.random.seed(42)
particles = np.random.random((10, 2))  # 10 particles, 2D
velocities = np.random.normal(0, 0.1, (10, 2))
pbest = particles.copy()
pbest_fitness = np.sum(particles, axis=1)
gbest = particles[np.argmax(pbest_fitness)]
velocities = 0.5 * velocities + 0.5 * (pbest - particles) + 0.5 * (gbest - particles)
particles += velocities
print("Global Best:", gbest)
```

## Output
```
Global Best: [0.68659274 0.5280433 ]
```

## Explanation
- **Particle Swarm Optimization**: Optimizes by moving particles toward personal and global bests.
- **Logic**: Updates velocities based on best positions and moves particles.
- **Complexity**: O(n*d) for n particles, d dimensions.
- **Use Case**: Used for function optimization in engineering or ML.
- **Best Practice**: Tune inertia/cognitive/social weights; bound particles; validate convergence.