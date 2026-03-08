# 0104-Numerical-Integration Cheatsheet

- **Trapezoidal rule** approximates ∫_a^b f(x) dx by dividing interval into n pieces:
  `h=(b-a)/n`, `sum = (f(a)+f(b))/2 + Σ_{i=1}^{n-1} f(a+i h)`; result = `h*sum`.
- **Simpson’s rule** uses quadratic interpolation on pairs of intervals:
  ```python
  h=(b-a)/n
  s=f(a)+f(b)
  for i in range(1,n):
      s += 4*f(a+i*h) if i%2 else 2*f(a+i*h)
  return s * h/3
  ```
  requires n even.
- Accuracy increases with n; error ~ O(h²) for trapezoid, O(h⁴) for Simpson.
- For vectorized functions, use NumPy arrays to compute f at multiple points.
- Adaptive integration splits intervals until desired tolerance met.
- Use `scipy.integrate.quad` for robust production-quality integration.
