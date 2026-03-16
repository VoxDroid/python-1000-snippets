# Fluid Simulation

## Description
This snippet demonstrates basic fluid-like simulation behaviors using grid-based diffusion and advection.

## Samples
- `SAMPLES/sample1.py`: Diffuse a scalar field on a grid using a simple stencil.
- `SAMPLES/sample2.py`: Advect a scalar field using a semi-Lagrangian scheme with a rotational velocity field.
- `SAMPLES/sample3.py`: Combine advection and diffusion for a simple fluid-like scalar simulation.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- These examples are simplified and work without external physics engines.
- Diffusion blends values with neighbors; advection transports values along a velocity field.
- For more advanced fluid simulation, consider Navier-Stokes solvers and pressure projection.
