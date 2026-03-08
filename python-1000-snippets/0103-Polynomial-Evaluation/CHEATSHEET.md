# 0103-Polynomial-Evaluation Cheatsheet

- Coefficients list `[a0, a1, ..., an]` corresponds to polynomial `a0 + a1 x + ... + an x^n`.
- Evaluate efficiently with Horner’s method:
  ```python
  result=0
  for coef in reversed(coeffs):
      result = result*x + coef
  ```
- Horner’s requires O(n) operations; avoids computing powers separately.
- Useful when evaluating polynomials many times, e.g. interpolation or root finding.
- Derivative can be computed similarly; evaluate derivative polynomial using coeffs*index.
- `numpy.polyval` and `numpy.polyder` provide vectorized operations.
