# Custom Exception Handling

## Description
This snippet demonstrates defining and using custom exception types to handle application-specific error conditions cleanly and consistently.

## Files
- `SAMPLES/sample1.py`: Validate numeric input using a custom exception.
- `SAMPLES/sample2.py`: Parse and validate a simple configuration dictionary.
- `SAMPLES/sample3.py`: Wrap and raise custom exceptions for third-party errors (e.g., file I/O).

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Result: 5
Config error: Missing required key 'timeout'
Caught custom file error: Failed to read config file
```

## Explanation
- **Custom exceptions**: Subclass `Exception` to represent domain-specific error types.
- **Logic**: Use `raise` with custom exception classes and `try/except` blocks to handle them.
- **Best practice**: Keep exception classes small and use clear messages; avoid catching generic `Exception` unless necessary.
