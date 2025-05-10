# Root Finding

## Description
This snippet finds a root of a function using the bisection method, assuming the root lies between two bounds.

## Code
```python
def bisection(f, a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        return None
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def f(x):
    return x**2 - 4  # Root at x=2

print("Root:", bisection(f, 0, 3))
```

## Output
```
Root: 2.0000000000000004
```

## Explanation
- **Bisection**: Repeatedly halves the interval `[a, b]` where `f(a) * f(b) < 0`, converging to a root.
- **Parameters**: `tol` is the tolerance for convergence.
- **Complexity**: O(log((b-a)/tol)) iterations.
- **Use Case**: Used in optimization, physics, or solving equations.
- **Best Practice**: Validate sign change; use Newton-Raphson for faster convergence if derivatives are available.