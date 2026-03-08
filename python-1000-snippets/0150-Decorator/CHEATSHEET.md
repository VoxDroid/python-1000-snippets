# 0150-Decorator Cheatsheet

- **Purpose**: modify or extend function behaviour without changing its code.
- **Syntax**: apply `@decorator` above a function definition or wrap manually `f = decorator(f)`.
- **Preserve metadata**: use `functools.wraps` inside wrapper.
- **Decorator with args**: define a function returning a decorator.
- **Multiple decorators**: stack with multiple `@` lines (inner-most applies first).

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """say hello"""
    return f"Hello, {name}"
```

- **Common uses**: logging, timing, caching, authentication.
- **Testing**: call decorated functions normally; metadata such as `__name__` should be preserved.
- **Performance**: adds small constant overhead; keep wrappers simple.

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
