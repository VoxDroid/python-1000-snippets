# Advanced Mocking Techniques

## Description
This snippet demonstrates mocking a function using `unittest.mock`.

## Code
```python
# Note: Requires `unittest.mock`
from unittest.mock import patch

def get_data():
    return "Real data"

try:
    with patch('__main__.get_data', return_value="Mocked data"):
        print(get_data())
except ImportError:
    print("Mock Output: Mocked data")
```

## Output
```
Mock Output: Mocked data
```
*(Real output with `unittest.mock`: `Mocked data`)*

## Explanation
- **Advanced Mocking Techniques**: Replaces a function’s behavior with a mock.
- **Logic**: Uses `patch` to mock `get_data` and return a custom value.
- **Complexity**: O(1) per mock.
- **Use Case**: Used to isolate dependencies in unit tests.
- **Best Practice**: Use specific patches; restore originals; test mock behavior.