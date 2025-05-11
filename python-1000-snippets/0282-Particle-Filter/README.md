# Particle Filter

## Description
This snippet demonstrates a simple Particle Filter using `numpy`.

## Code
```python
import numpy as np
np.random.seed(42)
N = 100
particles = np.random.normal(0, 1, N)
weights = np.ones(N) / N
z = 1.0  # Measurement
particles += np.random.normal(0, 0.1, N)  # Predict
weights *= np.exp(-0.5 * (particles - z)**2 / 0.1)
weights /= np.sum(weights)
indices = np.random.choice(N, N, p=weights)
particles = particles[indices]
print("Mean Estimate:", np.mean(particles))
```

## Output
```
Mean Estimate: 0.9735387616485346
```

## Explanation
- **Particle Filter**: Estimates state using a set of weighted particles.
- **Logic**: Predicts particle positions, updates weights, and resamples.
- **Complexity**: O(N) for N particles.
- **Use Case**: Used for non-linear or non-Gaussian tracking.
- **Best Practice**: Tune particle count; handle degeneracy; validate measurements.