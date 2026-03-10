# 0187-Mocking Cheatsheet

- **Purpose**: replace parts of your system under test with mock objects and make assertions about how they were used.
- **Core tool**: `unittest.mock` provides `Mock`, `patch`, `patch.object`, `MagicMock`.
- **Patch targets**: specify import path where object is looked up by the code under test, not where defined.
- **Common methods**: `mock.return_value`, `mock.side_effect`, `mock.assert_called_with()`.
- **Tips**: reset mocks between tests; use context managers or decorators for patching.

```bash
python3 SAMPLES/sample1.py
python3 -m unittest discover -s SAMPLES
```
