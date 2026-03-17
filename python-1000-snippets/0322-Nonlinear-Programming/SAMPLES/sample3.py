"""Nonlinear optimization with bounds.

Problem:
    minimize the Rosenbrock function in 2D:
      f(x, y) = (1 - x)^2 + 100*(y - x^2)^2
    with bounds: -2 <= x,y <= 2

Uses bounds to constrain the search region.
"""

import numpy as np

try:
    from scipy.optimize import minimize
except ImportError as e:
    raise SystemExit("scipy is required for this example. Install it with `pip install scipy`.") from e

# Rosenbrock function

def rosenbrock(z):
    x, y = z
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

bounds = [(-2, 2), (-2, 2)]

x0 = np.array([-1.0, 1.0])
res = minimize(rosenbrock, x0, bounds=bounds, method="L-BFGS-B")

print("Solution:", np.round(res.x, 6))
print("Objective:", np.round(res.fun, 6))
