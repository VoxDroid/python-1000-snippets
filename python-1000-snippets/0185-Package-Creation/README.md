# Package Creation

## Description
This snippet demonstrates creating and using a Python package with a simple module.

## Directory Structure
```
my_package/
├── __init__.py
└── utilities.py
```

## Code
```python
# my_package/utilities.py
def add(a, b):
    return a + b

# main.py
from my_package import utilities

print(utilities.add(2, 3))
```

## Output
```
5
```

## Explanation
- **Package Creation**: Defines a package `my_package` with an `__init__.py` (can be empty) and a `utilities` module.
- **Logic**: Imports and uses the `add` function from `utilities`.
- **Complexity**: O(1) for function call.
- **Use Case**: Used to organize related modules into a namespace.
- **Best Practice**: Include `__init__.py`; use relative imports within packages; document package purpose.