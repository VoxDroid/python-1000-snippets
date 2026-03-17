# 0340-Dynamic-Error-Management Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Batch processing with error collection
python SAMPLES/sample2.py  # Retry with exponential backoff
python SAMPLES/sample3.py  # Collect errors via context manager
```

## Tips
- Decide whether to fail fast or collect errors for downstream reporting.
- Use a list to accumulate errors when processing many items.
- Use retry loops with backoff for transient failures (e.g. network requests).
- Use `raise ... from e` to preserve exception context.

## Common patterns
- Collecting errors:
  ```python
results, errors = [], []
for item in items:
    try:
        results.append(process(item))
    except Exception as e:
        errors.append(str(e))
```
- Retry:
  ```python
for attempt in range(max_attempts):
    try:
        return operation()
    except TransientError:
        time.sleep(backoff)
```
- Context manager for error collection:
  ```python
with ErrorCollector() as collector:
    ...
``` 
