# 0339-Custom-Exception-Handling Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Basic custom exception usage
python SAMPLES/sample2.py  # Input validation config parsing
python SAMPLES/sample3.py  # Wrap external errors in custom exceptions
```

## Tips
- Create custom exceptions by subclassing `Exception`.
- Use `raise MyError("message")` to signal an error.
- Catch only the exceptions you expect, e.g., `except MyError as e:`.
- Preserve exception context using `raise ... from e` when wrapping.

## Common patterns
- Validation:
  ```python
if value <= 0:
    raise InvalidInputError("must be positive")
```
- Wrapping:
  ```python
try:
    do_something()
except IOError as e:
    raise FileProcessingError("...") from e
```
