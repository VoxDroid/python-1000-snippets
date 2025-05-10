# Polynomial Evaluation

## Description
This snippet evaluates a polynomial given its coefficients and a value of x using Horner’s method.

## Code
```python
def evaluate_polynomial(coeffs, x):
    result = 0
    for coef in reversed(coeffs):
        result = result * x + coef
    return result

coeffs = [1, 2, 3]  # 1 + 2x + 3x^2
x = 2
print(f"P({x}) =", evaluate_polynomial(coeffs, x))
```

## Output
```
P(2) = 17
```

## Explanation
- **Polynomial**: Represented as `coeffs[i] * x^i`; e.g., `[1, 2, 3]` is `1 + 2x + 3x²`.
- **Horner’s Method**: Efficiently computes `((3x + 2)x + 1)` for `x=2`.
- **Complexity**: O(n) time, where n is the degree.
- **Use Case**: Used in numerical analysis, graphics, or curve fitting.
- **Best Practice**: Validate coefficients; handle edge cases like empty lists.