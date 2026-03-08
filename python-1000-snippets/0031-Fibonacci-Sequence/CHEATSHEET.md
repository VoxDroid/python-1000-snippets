# Fibonacci Sequence Cheatsheet

## Iterative approach
```python
seq = [0,1]
for i in range(2,n):
    seq.append(seq[i-1]+seq[i-2])
```

## Recursive generator
```python
def fib(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b
```
```

## itertools alternative
```
import itertools
fib = itertools.accumulate(itertools.repeat(1), lambda x,y: x+y)
```

## Tips
- Use `yield` for memory efficiency.
- Handle zero or negative term counts gracefully.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py` (requires input)
3. `python SAMPLES/sample2.py` (requires input)
4. `python SAMPLES/sample3.py`

