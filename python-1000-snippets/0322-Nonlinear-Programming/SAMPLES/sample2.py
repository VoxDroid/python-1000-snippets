"""Nonlinear objective with equality constraint.

Problem:
    minimize f(x, y) = (x-2)^2 + (y+1)^2
    subject to x + 2y = 1

Uses SLSQP to satisfy constraint exactly.
"""

import numpy as np

try:
    from scipy.optimize import minimize
except ImportError as e:
    raise SystemExit("scipy is required for this example. Install it with `pip install scipy`.") from e

# Objective: shifted quadratic

def objective(z):
    x, y = z
    return (x - 2) ** 2 + (y + 1) ** 2

# Equality constraint: x + 2y = 1
constraint = {"type": "eq", "fun": lambda z: z[0] + 2 * z[1] - 1}

x0 = np.array([0.0, 0.0])
res = minimize(objective, x0, constraints=[constraint], method="SLSQP")

print("Solution:", np.round(res.x, 6))
print("Constraint (should be near 0):", np.round(constraint["fun"](res.x), 6))
print("Objective:", np.round(res.fun, 6))
