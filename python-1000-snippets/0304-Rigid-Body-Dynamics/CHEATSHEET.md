# 0304 - Rigid Body Dynamics Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Use Euler integration (`x += v*dt`, `v += a*dt`) for simple rigid body simulation.
- Maintain both linear and angular velocity for translation + rotation.
- Apply collision response by reflecting velocity and applying restitution.
- Keep the timestep small (e.g., 0.01) for stable integration.
