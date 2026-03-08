# 0102-Complex-Numbers Cheatsheet

- Use Python’s `complex(real, imag)` or literal `a + bj`.
- Basic operations: `+`, `-`, `*`, `/` behave as expected.
- Properties:
  - `z.conjugate()` returns conjugate.
  - `abs(z)` gives magnitude √(a²+b²).
  - `z.real` and `z.imag` access components.
- `cmath` module provides `phase(z)` (argument), `polar(z)`, `rect(r, phi)` for polar conversion, and exp/log/trig functions.
- Complex numbers handle engineering/scientific formulas, Fourier transforms, AC circuits.
