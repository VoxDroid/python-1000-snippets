# Chaos Engineering

## Description
This snippet demonstrates a chaos test by simulating failures.

## Code
```python
try:
    import random
    def chaos_test():
        if random.random() < 0.5:
            raise Exception("Chaos induced failure")
        return "Success"
    print("Result:", chaos_test())
except ImportError:
    print("Mock Output: Result: Success")
```

## Output
```
Mock Output: Result: Success
```
*(Real output: `Result: Success` or raises exception)*

## Explanation
- **Chaos Engineering**: Tests system resilience with random failures.
- **Logic**: Simulates a failure with 50% probability.
- **Complexity**: O(1) per test.
- **Use Case**: Used to validate system robustness.
- **Best Practice**: Start small; monitor impacts; automate tests.