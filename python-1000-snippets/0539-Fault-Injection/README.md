# Fault Injection

## Description
This snippet demonstrates injecting a fault into a function.

## Code
```python
try:
    def inject_fault(func):
        def wrapper():
            if True:  # Simulate fault
                raise ValueError("Injected fault")
            return func()
        return wrapper
    @inject_fault
    def normal():
        return "OK"
    print("Result:", normal())
except ImportError:
    print("Mock Output: Result: raises ValueError")
```

## Output
```
Mock Output: Result: raises ValueError
```
*(Real output: Raises `ValueError: Injected fault`)*

## Explanation
- **Fault Injection**: Introduces errors to test error handling.
- **Logic**: Wraps a function to raise an error.
- **Complexity**: O(1) per call.
- **Use Case**: Used in testing system resilience.
- **Best Practice**: Control fault triggers; log faults; test recovery.