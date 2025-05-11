# Cloth Simulation

## Description
This snippet demonstrates a simple cloth simulation using mass-spring model.

## Code
```python
import numpy as np
points = np.array([[0.0, 0.0], [1.0, 0.0]])  # Two points
velocities = np.zeros((2, 2))
spring_force = -10.0 * (np.linalg.norm(points[1] - points[0]) - 1.0) * (points[1] - points[0])
velocities[1] += spring_force * 0.1
points += velocities * 0.1
print("Updated Point:", points[1])
```

## Output
```
Updated Point: [1. 0.]
```

## Explanation
- **Cloth Simulation**: Simulates a spring between two points.
- **Logic**: Applies Hooke’s law to update positions via velocities.
- **Complexity**: O(n) for n points.
- **Use Case**: Used for cloth or soft body effects in games.
- **Best Practice**: Add damping; use grid of springs; handle collisions.