# Arithmetic Operations Cheatsheet

Quick reference for performing arithmetic in Python.

## Operators
- `+` addition
- `-` subtraction
- `*` multiplication
- `/` true division (always returns float)
- `//` floor division (rounds down to integer)
- `%` modulus (remainder)
- `**` exponentiation

## Examples
```python
a, b = 7, 4
print(a + b)      # 11
print(a - b)      # 3
print(a * b)      # 28
print(a / b)      # 1.75
print(a // b)     # 1
print(a % b)      # 3
print(a ** b)     # 2401
```

## Tips
- Use parentheses `()` to control evaluation order.
- Mixing ints and floats yields a float result.
- For large integers, Python automatically handles big numbers.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

