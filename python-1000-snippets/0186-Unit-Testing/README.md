# Unit Testing

## Description
This snippet demonstrates unit testing a simple function using the `unittest` module.

## Code
```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == "__main__":
    unittest.main()
```

## Output
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## Explanation
- **Unit Testing**: Uses `unittest` to test the `add` function with positive and negative inputs.
- **Logic**: `TestAdd` defines test cases; `assertEqual` checks expected vs. actual results.
- **Complexity**: O(1) per test case.
- **Use Case**: Used to verify code correctness and prevent regressions.
- **Best Practice**: Write focused tests; cover edge cases; run tests automatically.