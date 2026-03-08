# Directory Creation Cheatsheet

## os.mkdir vs makedirs
- `os.mkdir('a')` creates single directory
- `os.makedirs('a/b/c')` creates nested path

## pathlib alternative
```python
from pathlib import Path
Path('a/b').mkdir(parents=True, exist_ok=True)
```

## Tips
- Use `exist_ok=True` to avoid exceptions.
- Check `os.path.exists()` beforehand.

## Running samples
Activate venv and run `SAMPLES/sample*.py`.
