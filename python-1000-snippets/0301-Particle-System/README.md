# Particle System

## Description
This snippet demonstrates simple particle system behaviors using `numpy`.
It includes particle spawning, lifetimes, gravity, and boundary collisions.

## Samples
- `SAMPLES/sample1.py`: Particle system with lifetimes, automatic respawn.
- `SAMPLES/sample2.py`: Fountain-style particle emitter with gravity.
- `SAMPLES/sample3.py`: Bouncing particles with boundary collisions and damping.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Particle systems update positions based on velocity and apply simple forces.
- Use structured arrays for efficient particle attribute storage.
- Add rendering using a graphics library (Pygame, matplotlib, etc.) for visualization.
