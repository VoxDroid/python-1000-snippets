# Numerical Integration

## Description
This snippet performs numerical integration of a function using the trapezoidal rule.

## Code
```python
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

def f(x):
    return x**2  # Example: integrate x^2

a, b = 0, 1
n = 100
print("Integral:", trapezoidal_rule(f, a, b, n))
```

## Output
```
Integral: 0.33335000000000004
```

## Explanation
- **Trapezoidal Rule**: Approximates the integral by summing areas of trapezoids; `∫f(x)dx ≈ h * [(f(a) + f(b))/2 + Σf(a+ih)]`.
- **Parameters**: `a`, `b` are bounds; `n` is the number of intervals.
- **Complexity**: O(n) time.
- **Use Case**: Used in physics, engineering, or data analysis for integration.
- **Best Practice**: Increase `n` for accuracy; use libraries like SciPy for production.