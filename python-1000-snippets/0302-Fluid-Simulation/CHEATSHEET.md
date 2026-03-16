# 0302 - Fluid Simulation Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Diffusion spreads values to neighboring cells; use a 5-point stencil for explicit diffusion.
- Advection transports scalar values along a velocity field; semi-Lagrangian backtracing avoids CFL instability.
- Combine diffusion and advection for more realistic fluid-like behavior, but note this is not a full Navier-Stokes solver.
