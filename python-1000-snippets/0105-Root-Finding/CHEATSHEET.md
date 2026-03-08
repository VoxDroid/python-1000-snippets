# 0105-Root-Finding Cheatsheet

- The **bisection method** locates a root of continuous function f on [a,b] if f(a) and f(b) have opposite signs.
- Iteration:
  ```python
  while (b-a)/2 > tol:
      c = (a+b)/2
      if f(c)==0: return c
      if f(a)*f(c) < 0: b=c
      else: a=c
  return (a+b)/2
  ```
- Convergence is linear; number of iterations ≈ log2((b-a)/tol).
- Requires no derivative information; robust but slower than Newton.
- For functions without sign change, return None or raise error.
- Complement with **Newton-Raphson** when derivative available for quadratic convergence.
