# Modular Code Structure

## Description
This snippet demonstrates modular code with a simple package structure.

## Code
```python
# Simulated module: utils.py
def utility_function(x):
    return x * 2

# Main code
try:
    # Simulate importing from utils module
    utility = utility_function
    print(utility(5))
except NameError:
    print("Mock Output: 10")
```

## Output
```
10
```

## Explanation
- **Modular Code Structure**: Organizes code into reusable modules.
- **Logic**: Simulates a utility function import and usage.
- **Complexity**: O(1) per call.
- **Use Case**: Used for large projects to improve maintainability.
- **Best Practice**: Use clear module names; avoid circular imports; document modules.