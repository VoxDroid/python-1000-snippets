# 0312 - Particle Swarm Optimization Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Tune **inertia**, **cognitive**, and **social** coefficients for convergence.
- Track each particle’s personal best (`pbest`) and the swarm’s global best (`gbest`).
- Clamp velocities to avoid runaway particles.
- Use small time steps and enough particles for exploration.
