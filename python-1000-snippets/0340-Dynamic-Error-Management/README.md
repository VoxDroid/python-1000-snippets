# Dynamic Error Management

## Description
This snippet demonstrates advanced error-handling patterns where errors are collected, retried, or managed dynamically rather than immediately propagated.

## Files
- `SAMPLES/sample1.py`: Collect errors during batch processing and return both results and a list of issues.
- `SAMPLES/sample2.py`: Retry an operation with exponential backoff on transient errors.
- `SAMPLES/sample3.py`: Use a context manager to collect multiple errors and report them together.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Results: [5.0, 0, 3.3333333333333335], Errors: ['Division by zero']
Operation succeeded after 2 retries
Collected errors: ['Error A', 'Error B']
```

## Explanation
- **Dynamic error management**: Captures errors for later reporting instead of failing immediately.
- **Logic**: Use try/except blocks to catch errors and store them; implement retries for transient failures.
- **Use Case**: Useful in data pipelines, batch processing, network calls.
- **Best practice**: Do not swallow exceptions silently; log and surface errors appropriately.
