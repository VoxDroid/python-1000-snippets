# Reduce Function Cheatsheet

## Basic syntax
```python
from functools import reduce
reduce(func, iterable[, initializer])
```

## Tips
- `initializer` sets starting value and affects result type.
- Common alternatives: `sum()`, `math.prod()`, `''.join()` for strings.

## Examples
```python
reduce(lambda a,b: a+b, [1,2,3], 0)
```

## Running samples
Activate virtual env then run `SAMPLES/sample*.py`.
