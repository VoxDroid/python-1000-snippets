# Directory Listing Cheatsheet

## Basic listing
```python
import os
print(os.listdir(path))
```

## Recursive
```python
for root, dirs, files in os.walk(path):
    print(root, files)
```

## scandir
```python
with os.scandir(path) as it:
    for entry in it:
        print(entry.name, entry.is_file())
```

## Filtering
- Use `fnmatch` or list comprehension.

## Tips
- `os.listdir` returns names; join with `os.path.join` for full path.
- `os.walk` can be limited with `topdown` flag.

## Running samples
Activate venv and execute `SAMPLES/sample*.py`.
