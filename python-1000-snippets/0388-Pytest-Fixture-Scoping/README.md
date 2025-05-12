# Pytest Fixture Scoping

## Description
This snippet demonstrates pytest fixtures with function scope.

## Code
```python
# Note: Requires `pytest`. Install with `pip install pytest`
try:
    import pytest
    @pytest.fixture(scope="function")
    def setup():
        return "Setup"
    
    def test_example(setup):
        assert setup == "Setup"
    
    print("Fixture would be created per test")
except ImportError:
    print("Mock Output: Fixture would be created per test")
```

## Output
```
Mock Output: Fixture would be created per test
```
*(Real output with `pytest`: No console output, fixture runs per test)*

## Explanation
- **Pytest Fixture Scoping**: Defines a function-scoped fixture for tests.
- **Logic**: `setup` fixture provides data for each test function.
- **Complexity**: O(1) per fixture invocation.
- **Use Case**: Used to provide test setup/teardown logic.
- **Best Practice**: Choose appropriate scope; minimize fixture complexity; test fixtures.