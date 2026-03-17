# Computational Fluid Dynamics

## Description
This snippet provides simple 2D CFD examples using finite differences and NumPy. The examples are educational and demonstrate diffusion and viscous flow updates.

## Files
- `SAMPLES/sample1.py`: 2D diffusion (heat equation) on a grid.
- `SAMPLES/sample2.py`: 2D viscous Burgers' equation (velocity field evolution).
- `SAMPLES/sample3.py`: Simple incompressible flow step with pressure Poisson solve.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Center temp: 0.43
Center u: 0.37, v: 0.02
Max velocity magnitude: 0.28
```

## Explanation
- **Finite differences**: Use explicit updates for diffusion and advection.
- **Burgers' equation**: Models viscous momentum transport and nonlinear advection.
- **Pressure Poisson**: Enforces incompressibility by solving a Poisson equation for pressure.
- **Use Case**: Basis for CFD solvers and fluid flow visualization.
