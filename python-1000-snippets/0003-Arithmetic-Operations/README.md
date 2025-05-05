# Arithmetic Operations

## Description
This snippet demonstrates basic arithmetic operations in Python, including addition, subtraction, multiplication, division, and more. It showcases how Python handles numerical calculations.

## Code
```python
a = 10
b = 3
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
modulus = a % b
exponentiation = a ** b
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Floor Division: {floor_division}")
print(f"Modulus: {modulus}")
print(f"Exponentiation: {exponentiation}")
```

## Output
```
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Floor Division: 3
Modulus: 1
Exponentiation: 1000
```

## Explanation
- **Operators**:
  - `+`: Adds two numbers.
  - `-`: Subtracts the second number from the first.
  - `*`: Multiplies two numbers.
  - `/`: Divides the first number by the second (returns a float).
  - `//`: Floor division, divides and rounds down to the nearest integer.
  - `%`: Modulus, returns the remainder of division.
  - `**`: Exponentiation, raises the first number to the power of the second.
- **Variables**: `a` and `b` are integers used as operands.
- **f-strings**: The `f"..."` syntax (f-strings) allows embedding variable values in strings for clean output formatting.
- **Use Case**: Arithmetic operations are essential for calculations in applications like finance, scientific computing, and game development.
- **Precision**: Division (`/`) returns a float, even if the result is a whole number, which is important for accurate computations.