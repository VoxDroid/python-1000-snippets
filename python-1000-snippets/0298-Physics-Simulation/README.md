# Physics Simulation

## Description
This snippet demonstrates a simple physics simulation using `pybullet`.

## Code
```python
# Note: Requires `pybullet`. Install with `pip install pybullet`
try:
    import pybullet as p
    p.connect(p.DIRECT)
    p.setGravity(0, 0, -10)
    p.loadURDF("plane.urdf")
    ball = p.loadURDF("sphere2.urdf", [0, 0, 1])
    p.stepSimulation()
    pos, _ = p.getBasePositionAndOrientation(ball)
    print("Ball Position:", pos)
    p.disconnect()
except ImportError:
    print("Mock Output: Ball Position: (0.0, 0.0, 0.9)")
```

## Output
```
Mock Output: Ball Position: (0.0, 0.0, 0.9)
```
*(Real output with `pybullet`: `Ball Position: (<x>, <y>, <z around 0.9>)`)*

## Explanation
- **Physics Simulation**: Simulates a falling ball with gravity.
- **Logic**: Sets up a plane, adds a ball, and steps the simulation.
- **Complexity**: O(1) per step (physics engine varies).
- **Use Case**: Used for game physics or robotics.
- **Best Practice**: Tune gravity; use realistic models; validate dynamics.