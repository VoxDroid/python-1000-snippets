# Molecular Dynamics

## Description
This snippet implements a simple 2D molecular dynamics (MD) simulation using Lennard-Jones interactions and velocity Verlet integration.

## Files
- `SAMPLES/sample1.py`: Three particles interacting with a Lennard-Jones potential.
- `SAMPLES/sample2.py`: Computes pairwise potential energy and radial distribution after simulation.
- `SAMPLES/sample3.py`: Uses a simple thermostat to maintain temperature while simulating dynamics.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Particle positions:
[[0.30 0.27]
 [1.06 0.79]
 [0.47 1.78]]
Total energy: -2.31
Average kinetic energy: 0.05
```

## Explanation
- **Lennard-Jones potential** models attraction and repulsion between particles.
- **Velocity Verlet** integration updates positions and velocities in a time-reversible manner.
- **Thermostat** can be used to control temperature (kinetic energy).
- **Use Case**: Molecular simulation, materials science, statistical mechanics.
