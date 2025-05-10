# Mocking

## Description
This snippet demonstrates mocking a function using `unittest.mock` to test code with dependencies.

## Code
```python
from unittest.mock import patch
import unittest

def get_data():
    return "Real data"

def process_data():
    return f"Processed: {get_data()}"

class TestProcessData(unittest.TestCase):
    @patch("module.get_data")
    def test_process_data(self, mock_get_data):
        mock_get_data.return_value = "Mocked data"
        self.assertEqual(process_data(), "Processed: Mocked data")

if __name__ == "__main__":
    unittest.main()
```

## Output
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## Explanation
- **Mocking**: Uses `@patch` to replace `get_data` with a mock returning `"Mocked data"`.
- **Logic**: Tests `process_data` without calling the real `get_data`.
- **Complexity**: O(1) for the test.
- **Use Case**: Used to isolate code from external dependencies like APIs or databases.
- **Best Practice**: Mock only necessary dependencies; verify mock interactions.