# 0186-Unit-Testing Cheatsheet

- **Module**: use the built-in `unittest` framework.
- **Test case**: subclass `unittest.TestCase` and add methods starting with `test_`.
- **Assertions**: `assertEqual`, `assertTrue`, `assertRaises`, etc.
- **Running tests**: `python -m unittest` (discovers `test*.py`) or call `unittest.main()` in file.
- **Fixtures**: implement `setUp`/`tearDown` methods for common setup/cleanup.
- **Tips**: keep tests small and deterministic; run frequently (e.g., pre-commit).

```bash
python3 SAMPLES/sample1.py
python3 -m unittest discover -s SAMPLES
```
