# 0482-Particle Swarm Simulation Cheatsheet

## Quick Start
Run a sample:
```bash
python3 python-1000-snippets/0482-Particle-Swarm-Simulation/SAMPLES/sample1.py
```

## Notes
- PSO is a population-based optimization algorithm. Each particle has a position and velocity.
- `sample1.py` minimizes x^2 + y^2.
- `sample2.py` tracks history while minimizing (x-1)^2 + (y+2)^2.
- `sample3.py` applies PSO to the Rosenbrock function.

## Tips
- Increase `swarmsize` and `maxiter` for harder problems.
- Adjust `w`, `c1`, `c2` to control exploration vs exploitation.
- Use the output history for convergence diagnostics.
