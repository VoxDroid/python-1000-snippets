# Complex Numbers

## Description
This snippet demonstrates operations with complex numbers using Python’s built-in `complex` type.

## Code
```python
def complex_operations(z1, z2):
    return {
        "Addition": z1 + z2,
        "Multiplication": z1 * z2,
        "Conjugate of z1": z1.conjugate(),
        "Magnitude of z1": abs(z1)
    }

z1 = complex(3, 4)
z2 = complex(1, 2)
results = complex_operations(z1, z2)
for op, result in results.items():
    print(f"{op}: {result}")
```

## Output
```
Addition: (4+6j)
Multiplication: (-5+10j)
Conjugate of z1: (3-4j)
Magnitude of z1: 5.0
```

## Explanation
- **Complex Numbers**: Represented as `a + bj`, where `a` is real, `b` is imaginary.
- **Operations**:
  - Addition: `(a+bi) + (c+di) = (a+c) + (b+d)i`.
  - Multiplication: `(a+bi)(c+di) = (ac-bd) + (ad+bc)i`.
  - Conjugate: `a+bi → a-bi`.
  - Magnitude: `sqrt(a² + b²)`.
- **Use Case**: Used in signal processing, quantum mechanics, or electrical engineering.
- **Best Practice**: Use Python’s `complex` type; validate inputs for robustness.