# Lambda Function Cheatsheet

## Syntax
```python
lambda args: expression
```

## Common uses
- `map(lambda x: x*2, seq)`
- `filter(lambda x: x%2==0, seq)`
- `sorted(seq, key=lambda x: x[1])`

## Tips
- Good for short, throwaway functions.
- Can capture variables from enclosing scope (closure).
- Avoid overcomplicating; prefer `def` for readability.

## Running samples
Activate venv and execute `SAMPLES/sample*.py`.
