# Prime Number Check Cheatsheet

## Basic algorithm
```python
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        return False
return n > 1
```

## Optimization
- Only test up to sqrt(n).
- Skip even numbers after checking 2: `for i in range(3, ..., 2):`

## Tips
- Use `sympy.isprime()` for large numbers (external library).
- Non-integers or n<=1 are not prime.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py` (input required)
3. `python SAMPLES/sample2.py` (input required)
4. `python SAMPLES/sample3.py` (input required)

