# Robot Kinematics

## Description
This snippet demonstrates forward/inverse kinematics for a simple 2-link planar robot arm using NumPy.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
End effector position: [1.366 0.966]
Jacobian:
 [[-1.366 -0.966]
 [ 0.966  0.966]]
```

## Explanation
- **Forward Kinematics**: Computes end-effector position from joint angles.
- **Inverse Kinematics**: Uses a Jacobian-transpose iterative method to solve for joint angles given a target position.
- **Trajectory Generation**: Computes a sequence of end-effector positions from a joint-space path.
- **Best Practice**: Check reachability, handle singularities, and validate solutions against physical constraints.
