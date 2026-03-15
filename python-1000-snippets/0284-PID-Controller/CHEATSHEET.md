# 0284 - PID Controller Cheatsheet

## Quick Commands
```bash
pip install numpy
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- PID output: `u = Kp*e + Ki*integral + Kd*derivative`.
- Integral windup can be mitigated by clamping the integral term.
- Use a small simulation timestep (`dt`) for stability.
- Tune `Kp`, `Ki`, and `Kd` to adjust response speed, steady-state error, and damping.
