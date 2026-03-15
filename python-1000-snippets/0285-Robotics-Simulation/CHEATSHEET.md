# 0285 - Robotics Simulation Cheatsheet

## Quick Commands
```bash
pip install numpy
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Differential-drive kinematics: linear velocity = (v_r + v_l)/2, angular velocity = (v_r - v_l)/wheel_base.
- Forward kinematics for a planar arm: use cosine/sine of joint angles to compute end-effector position.
- Simple path planning can use greedy strategies, but robust planners (A*, RRT) handle obstacles better.
