# 0298-Physics-Simulation Cheatsheet

## Quick Start
- Run a sample:
  - `python python-1000-snippets/0298-Physics-Simulation/SAMPLES/sample1.py`
  - `python python-1000-snippets/0298-Physics-Simulation/SAMPLES/sample2.py`
  - `python python-1000-snippets/0298-Physics-Simulation/SAMPLES/sample3.py`

## Concepts
- **Numerical Integration**: Update state over time using small time steps (Euler integration).
- **Forces**: Compute acceleration from forces (gravity, drag, springs) and update velocity.
- **Collision Handling**: Detect and respond to boundaries or object collisions.

## Tips
- Use smaller time steps for more accurate simulations.
- For stable oscillations, consider symplectic integrators like semi-implicit Euler.
- Visualize trajectories with plotting libraries (matplotlib) for deeper insight.
