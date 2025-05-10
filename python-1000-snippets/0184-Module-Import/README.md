# Module Import

## Description
This snippet demonstrates importing and using a custom module with a simple function.

## Code
```python
# Assume a module named `utils.py` with:
# def greet(name):
#     return f"Hello, {name}!"

import utils

print(utils.greet("Alice"))
```

## Output
```
Hello, Alice!
```

## Explanation
- **Module Import**: Imports a hypothetical `utils` module and calls its `greet` function.
- **Logic**: Demonstrates module access using dot notation.
- **Complexity**: O(1) for function call.
- **Use Case**: Used to organize code into reusable modules.
- **Best Practice**: Use explicit imports; avoid circular imports; ensure module is in `sys.path`.