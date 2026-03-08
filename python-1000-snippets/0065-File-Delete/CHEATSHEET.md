# File Delete Cheatsheet

## Deleting files
```
import os
os.remove('file.txt')
# or os.unlink('file.txt')
```

## Directory removal
- `os.rmdir()` removes empty directories
- `shutil.rmtree()` removes directory tree

## Tips
- Use `os.path.exists()` before deleting.
- Use `try/except` to catch `FileNotFoundError`.

## Running samples
Activate venv and run scripts in `SAMPLES/`.
