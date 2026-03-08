# List Comprehension Cheatsheet

## Syntax
```python
[expression for item in iterable if condition]
```

## Examples
```python
nums = [1,2,3]
squares = [x*x for x in nums]
evens = [x for x in nums if x%2==0]
```

## Nested
```python
[(i,j) for i in range(3) for j in range(3)]
```

## Tips
- Comprehensions are faster and more concise than loops for simple tasks.
- Avoid heavy logic inside comprehensions; prefer loops for clarity.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

