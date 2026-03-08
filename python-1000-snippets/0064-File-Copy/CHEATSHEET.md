# File Copy Cheatsheet

## Functions
- `shutil.copy(src, dst)` copy data and permissions
- `shutil.copyfile(src, dst)` copy data only
- `shutil.copy2(src, dst)` copy with metadata
- `shutil.move(src, dst)` move/rename

## Tips
- Ensure destination directory exists.
- Use `os.path.exists()` to check.

## Example
```python
import shutil
shutil.copy('a.txt', 'b.txt')
```

## Running samples
Activate venv and run the sample scripts; inspect created files.
