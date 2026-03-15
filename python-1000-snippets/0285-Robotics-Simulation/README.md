# Robotics Simulation

## Description
This snippet demonstrates basic robotics simulation concepts using purely numerical models (no physics engine required).
The examples include differential-drive kinematics, forward kinematics for a planar arm, and simple grid-based path planning.

## Dependencies
- `numpy`

Install with:
```bash
pip install numpy
```

## Samples
- `SAMPLES/sample1.py`: Simulate a differential-drive robot moving in 2D.
- `SAMPLES/sample2.py`: Compute forward kinematics for a two-link planar robot arm.
- `SAMPLES/sample3.py`: Perform simple greedy path planning on a grid with obstacles.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Differential drive uses wheel velocities to compute linear and angular motion.
- Forward kinematics maps joint angles to end-effector coordinates.
- Path planning can be made more robust with algorithms like A* or RRT.
