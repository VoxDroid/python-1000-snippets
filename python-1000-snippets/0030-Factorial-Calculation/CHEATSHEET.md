# Factorial Calculation Cheatsheet

## Iterative implementation
```python
fact = 1
for i in range(1, n+1):
    fact *= i
```

## Recursive implementation
```python
def fact(n):
    return 1 if n <= 1 else n * fact(n-1)
```

## Using math module
```python
import math
math.factorial(n)
```

## Tips
- Factorial grows fast; watch for overflow (Python handles big ints).
- Negative inputs are not defined.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py` (input required)
3. `python SAMPLES/sample2.py` (input required)
4. `python SAMPLES/sample3.py`

