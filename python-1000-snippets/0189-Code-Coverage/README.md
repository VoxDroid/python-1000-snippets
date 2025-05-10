# Code Coverage

## Description
This snippet demonstrates measuring code coverage using `pytest` and `pytest-cov`.

## Code
```python
# math_ops.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# test_math_ops.py
def test_add():
    assert add(2, 3) == 5
```

## Output
*(Run with `pytest --cov=math_ops test_math_ops.py`)*
```
=========================== test session starts ===========================
plugins: cov-4.1.0
collected 1 item

test_math_ops.py .                                                 [100%]

---------- coverage: platform linux, python 3.9.5-final-0 -----------
Name          Stmts   Miss  Cover
---------------------------------
math_ops.py       2      1    50%
---------------------------------
TOTAL             2      1    50%
============================ 1 passed in 0.01s ============================
```

## Explanation
- **Code Coverage**: Uses `pytest-cov` to measure which lines of `math_ops.py` are executed by tests.
- **Logic**: Tests only `add`; `subtract` is untested, lowering coverage.
- **Complexity**: O(1) per test for coverage tracking.
- **Use Case**: Used to identify untested code and improve test suites.
- **Best Practice**: Aim for high coverage; install `pytest-cov` (`pip install pytest-cov`); ignore irrelevant files.