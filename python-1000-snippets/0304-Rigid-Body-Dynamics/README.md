# Rigid Body Dynamics

## Description
This snippet implements a simple 2D rigid body physics simulation (position + rotation) using Euler integration.

## Files
- `SAMPLES/sample1.py`: Drops a box under gravity and prints the final position and rotation.
- `SAMPLES/sample2.py`: Applies a continuous torque to rotate a box and prints the angular velocity.
- `SAMPLES/sample3.py`: Simulates bouncing on the ground with restitution and prints peak height values.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Final pos: (0.50, 0.00), angle: 0.23 rad
Final angular velocity: 2.85 rad/s
Peak bounce height: 0.76
```

## Explanation
- **Rigid body state**: position, angle, linear velocity, angular velocity.
- **Forces**: gravity affects linear motion; torques affect rotation.
- **Collision handling**: simple ground restitution is applied when the box hits y=0.
