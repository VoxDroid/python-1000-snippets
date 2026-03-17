# 0307 - Computational Fluid Dynamics Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Use a small timestep (`dt`) to maintain stability for explicit schemes.
- Diffusion can be modeled with a 5-point stencil (Laplace operator).
- Burgers' equation combines advection (nonlinear) with diffusion.
- For incompressible flow, enforce divergence-free velocity using a pressure Poisson solve.
