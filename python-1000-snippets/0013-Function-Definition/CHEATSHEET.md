# Function Definition Cheatsheet

## Defining functions
```python
def func(param1, param2=0):
    """Docstring describing function"""
    return param1 + param2
```

## Parameters
- Positional, keyword, default, `*args`, `**kwargs`.
- Type hints can be used: `def f(x: int) -> str:`

## Calling
- Positional: `f(1, 2)`
- Keyword: `f(param2=2, param1=1)`

## Examples
```python
def greet(name="World"):
    print(f"Hello, {name}")
```

## Tips
- Functions should do one thing and be reusable.
- Use `return` to send results back (see snippet 0014).

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

