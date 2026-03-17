# Soft Body Dynamics

## Description
This snippet implements a soft body using a network of mass points connected by springs. The system behaves like a deformable object (jelly) under gravity and external forces.

## Files
- `SAMPLES/sample1.py`: Two-point spring system (simple soft body) with gravity.
- `SAMPLES/sample2.py`: 2D soft body grid demonstrates deformation under gravity.
- `SAMPLES/sample3.py`: Applies an impulse and reports deformation metrics.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Point 1 pos: [0. 0.]
Point 2 pos: [0. 1.9]
Center displacement: 0.08
Max spring stretch: 0.02
```

## Explanation
- **Mass-spring system**: Each edge between points acts as a spring; rest lengths are preserved via constraint relaxation.
- **Damping**: Stabilizes the simulation by reducing velocity over time.
- **Deformation**: Measured via spring stretch/length changes.
- **Use Case**: Soft bodies, jelly, and other deformable objects.
