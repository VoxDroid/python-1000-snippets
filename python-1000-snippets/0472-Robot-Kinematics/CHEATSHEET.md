# 0472-Robot-Kinematics Cheatsheet

## Quick Tips
- Use forward kinematics to compute end-effector (x,y) given joint angles.
- Inverse kinematics can be solved iteratively; validate against reachability and avoid singularities.
- A Jacobian relates joint-angle rate to end-effector velocity; its transpose can be used for simple IK updates.

## Running examples
- `python SAMPLES/sample1.py` — forward kinematics and Jacobian.
- `python SAMPLES/sample2.py` — inverse kinematics via Jacobian-transpose updates.
- `python SAMPLES/sample3.py` — generate a joint-space trajectory and compute end-effector path.
