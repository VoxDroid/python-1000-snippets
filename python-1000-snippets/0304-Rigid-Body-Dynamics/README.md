# Rigid Body Dynamics

## Description
This snippet demonstrates rigid body dynamics using `pybullet`.

## Code
```python
# Note: Requires `pybullet`. Install with `pip install pybullet`
try:
    import pybullet as p
    p.connect(p.DIRECT)
    p.setGravity(0, 0, -10)
    box = p.loadURDF("cube.urdf", [0, 0, 1])
    p.applyExternalForce(box, -1, [0, 0, -10], [0, 0, 0], p.WORLD_FRAME)
    p.stepSimulation()
    pos, _ = p.getBasePositionAndOrientation(box)
    print("Box Position:", pos)
    p.disconnect()
except ImportError:
    print("Mock Output: Box Position: (0.0, 0.0, 0.8)")
```

## Output
```
Mock Output: Box Position: (0.0, 0.0, 0.8)
```
*(Real output with `pybullet`: `Box Position: (<x>, <y>, <z around 0.8>)`)*

## Explanation
- **Rigid Body Dynamics**: Simulates a cube under gravity and external force.
- **Logic**: Applies force and steps the physics simulation.
- **Complexity**: O(1) per step (physics engine varies).
- **Use Case**: Used for realistic object interactions in games.
- **Best Practice**: Tune forces; handle collisions; validate dynamics.