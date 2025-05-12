# Robot Kinematics

## Description
This snippet demonstrates forward kinematics for a 2D robot arm using `numpy`.

## Code
```python
try:
    import numpy as np
    def forward_kinematics(theta1, theta2, l1=1, l2=1):
        x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
        y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)
        return x, y
    x, y = forward_kinematics(np.pi/4, np.pi/4)
    print("Position:", (x, y))
except ImportError:
    print("Mock Output: (np.float64(0.7071067811865477), np.float64(1.7071067811865475))")
```

## Output
```
Mock Output: Position: (np.float64(0.7071067811865477), np.float64(1.7071067811865475))
```
*(Real output with `numpy`: `Position: (np.float64(0.7071067811865477), np.float64(1.7071067811865475))`)*

## Explanation
- **Robot Kinematics**: Computes the end-effector position of a 2D arm.
- **Logic**: Uses trigonometry to calculate coordinates from joint angles.
- **Complexity**: O(1) per calculation.
- **Use Case**: Used in robotic arm control or simulation.
- **Best Practice**: Validate angles; handle singularities; test with real hardware.