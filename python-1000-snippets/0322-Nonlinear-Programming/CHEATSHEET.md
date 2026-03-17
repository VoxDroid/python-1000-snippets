# 0322-Nonlinear-Programming Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Use `scipy.optimize.minimize` for general constrained nonlinear problems.
- Constraints can be:
  - **Equality**: functions that must equal 0.
  - **Inequality**: functions that must be >= 0.
- Use `bounds=[(low, high), ...]` to restrict variable ranges.
- Common methods:
  - `SLSQP`: supports bounds and both equality/inequality constraints.
  - `trust-constr`: good for larger problems with gradients.
- Provide a good initial guess for faster convergence.

## Example outline
```python
from scipy.optimize import minimize

# objective
f = lambda x: ...

# constraints
g = {'type': 'eq', 'fun': lambda x: ...}

# bounds
b = [(0, 1), (None, 5)]

res = minimize(f, x0=[0,0], constraints=[g], bounds=b)
print(res.x)
```
