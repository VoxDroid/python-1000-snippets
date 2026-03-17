"""Minimize a quadratic objective subject to a linear equality constraint.

Problem:
    minimize f(x, y) = (x-1)^2 + (y-2)^2
    subject to x + y = 3

This is a convex, constrained nonlinear optimization problem.
"""

import numpy as np

try:
    from scipy.optimize import minimize
except ImportError as e:
    raise SystemExit("scipy is required for this example. Install it with `pip install scipy`.") from e

# Objective: quadratic bowl centered at (1, 2)
def objective(z):
    x, y = z
    return (x - 1) ** 2 + (y - 2) ** 2

# Constraint: x + y == 3
constraint = {"type": "eq", "fun": lambda z: z[0] + z[1] - 3}

# Start at a guess and minimize
x0 = np.array([0.5, 0.5])
res = minimize(objective, x0, constraints=[constraint], method="SLSQP")

print("Solution:", np.round(res.x, 6))
print("Objective:", np.round(res.fun, 6))
