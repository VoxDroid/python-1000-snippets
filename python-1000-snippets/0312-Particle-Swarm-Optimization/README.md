# Particle Swarm Optimization

## Description
This snippet implements a basic Particle Swarm Optimization (PSO) algorithm in pure Python. PSO searches for the minimum of a function by moving a swarm of particles based on personal and global best positions.

## Files
- `SAMPLES/sample1.py`: Minimize a 2D sphere function (sum of squares) with PSO.
- `SAMPLES/sample2.py`: Minimize a quadratic bowl with a known optimum.
- `SAMPLES/sample3.py`: Optimize a multimodal function (Rastrigin-like).

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Best position: [0.02 0.01], fitness: 0.0005
Best position: [1.00 -2.00], fitness: 0.0000
Best position: [0.01], fitness: 0.01
```

## Explanation
- **Particles**: Each has a position and velocity in parameter space.
- **Personal best (pbest)**: Best position each particle has visited.
- **Global best (gbest)**: Best position found by the swarm.
- **Update rules**: Velocity is updated based on inertia, cognitive (pbest), and social (gbest) components.
