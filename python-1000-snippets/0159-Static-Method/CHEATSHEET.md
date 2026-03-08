# 0159-Static-Method Cheatsheet

- **Purpose**: define methods inside a class namespace that do not access instance (`self`) or class (`cls`).
- **Syntax**: decorate with `@staticmethod`; method takes no special first argument.
- **Call**: can be invoked on class (`C.method()`) or instance (`c.method()`).
- **Use cases**: utility functions, factories, validation helpers.
- **Difference**: unlike `@classmethod`, static methods don’t receive class reference.

```python
class C:
    @staticmethod
    def f(x):
        return x*2

print(C.f(3))
```

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
