# 0337-File-System-Operations Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # List files and sizes
python SAMPLES/sample2.py  # Walk a directory tree
python SAMPLES/sample3.py  # Create/remove temp file in /temp
```

## Tips
- Use `pathlib.Path` for cross-platform path operations.
- Use `rglob()` to recursively search for files matching a pattern.
- Use `/temp` for temporary outputs in this repo so cleanup is easy.

## Common patterns
- List files:
  ```python
  list(Path('.').iterdir())
  ```
- Recursively find files:
  ```python
  list(Path('.').rglob('*.py'))
  ```
- Create a temp directory:
  ```python
  Path('/temp').mkdir(exist_ok=True)
  ```
