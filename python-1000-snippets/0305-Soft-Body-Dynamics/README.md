# Soft Body Dynamics

## Description
This snippet demonstrates soft body dynamics using a simple spring-mass system.

## Code
```python
import numpy as np
points = np.array([[0.0, 0.0], [1.0, 0.0]])
velocities = np.zeros((2, 2))
force = -10.0 * (np.linalg.norm(points[1] - points[0]) - 0.5) * (points[1] - points[0])
velocities[1] += force * 0.1
points += velocities * 0.1
print("Soft Body Point:", points[1])
```

## Output
```
Soft Body Point: [0.95 0. ]
```

## Explanation
- **Soft Body Dynamics**: Simulates a deformable object with springs.
- **Logic**: Updates a point’s position based on spring forces.
- **Complexity**: O(n) for n points.
- **Use Case**: Used for soft objects like jelly or rubber in simulations.
- **Best Practice**: Add damping; use tetrahedral meshes; handle collisions.