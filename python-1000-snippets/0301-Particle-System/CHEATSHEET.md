# 0301 - Particle System Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Store particle attributes in numpy arrays for efficient vectorized updates.
- Manage particle lifetimes and respawn dead particles to keep the system running.
- Apply forces (gravity, wind) by modifying velocities before updating positions.
- For collisions, reflect velocity components against boundaries and apply damping.
