# Parameterized Unit Tests

## Description
This snippet demonstrates parameterized unit tests using `pytest`.

## Code
```python
# Note: Requires `pytest`. Install with `pip install pytest`
def add(a, b):
    return a + b

try:
    import pytest
    @pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (0, 0, 0), (-1, 1, 0)])
    def test_add(a, b, expected):
        assert add(a, b) == expected
    print("Tests would run successfully")
except ImportError:
    print("Mock Output: Tests would run successfully")
```

## Output
```
Mock Output: Tests would run successfully
```
*(Real output with `pytest`: Test results, typically no console output)*

## Explanation
- **Parameterized Unit Tests**: Runs tests with multiple input sets.
- **Logic**: Uses `pytest.mark.parametrize` to test `add` function.
- **Complexity**: O(n) for n test cases.
- **Use Case**: Used to test functions with varied inputs.
- **Best Practice**: Cover edge cases; keep tests independent; use fixtures.