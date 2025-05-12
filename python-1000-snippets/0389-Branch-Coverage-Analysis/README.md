# Branch Coverage Analysis

## Description
This snippet demonstrates a function for branch coverage analysis.

## Code
```python
# Note: Requires `coverage`. Install with `pip install coverage`
def check_value(x):
    if x > 0:
        return "Positive"
    else:
        return "Non-positive"

try:
    import coverage
    print("Function ready for coverage analysis")
except ImportError:
    print("Mock Output: Function ready for coverage analysis")
```

## Output
```
Mock Output: Function ready for coverage analysis
```
*(Real output with `coverage`: No console output, used with coverage tool)*

## Explanation
- **Branch Coverage Analysis**: Provides a function testable for branch coverage.
- **Logic**: `check_value` has two branches for positive/non-positive inputs.
- **Complexity**: O(1) per call.
- **Use Case**: Used to ensure all code paths are tested.
- **Best Practice**: Use coverage tools; test all branches; combine with unit tests.