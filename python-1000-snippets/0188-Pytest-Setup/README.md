# Pytest Setup

## Description
This snippet demonstrates setting up and running tests with `pytest`.

## Code
```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

## Output
*(Run with `pytest test_math.py`)*
```
=========================== test session starts ===========================
collected 1 item

test_math.py .                                                     [100%]

============================ 1 passed in 0.01s ============================
```

## Explanation
- **Pytest Setup**: Defines a test file with a simple `test_add` function using assertions.
- **Logic**: `pytest` discovers and runs tests automatically.
- **Complexity**: O(1) per test.
- **Use Case**: Used for flexible, scalable testing in projects.
- **Best Practice**: Name test files/functions with `test_`; use fixtures for setup; install `pytest` (`pip install pytest`).