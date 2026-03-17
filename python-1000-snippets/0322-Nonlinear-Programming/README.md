# Nonlinear Programming

## Description
This snippet uses SciPy to solve small nonlinear optimization problems with constraints.

## Files
- `SAMPLES/sample1.py`: Minimize a quadratic subject to a linear constraint.
- `SAMPLES/sample2.py`: Constrained optimization using equality constraint.
- `SAMPLES/sample3.py`: Optimize a nonlinear objective with bounds.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Solution: [0. 0.]
Solution: [1. 1.]
Solution: [0.5 0.5]
```

## Explanation
- **Nonlinear programming**: Deals with nonlinear objective functions and constraints.
- **SciPy's `minimize`**: Supports different methods like SLSQP, trust-constr, etc.
- **Constraints**: Can include equality, inequality, and bounds.
- **Use Case**: Engineering design, parameter fitting, resource allocation.
