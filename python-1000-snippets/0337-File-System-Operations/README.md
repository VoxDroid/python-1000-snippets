# File System Operations

## Description
This snippet demonstrates common file system operations (listing, searching, and managing files) using `pathlib` and `os`.

## Files
- `SAMPLES/sample1.py`: List directory contents and show file sizes.
- `SAMPLES/sample2.py`: Walk a directory tree and collect filenames by extension.
- `SAMPLES/sample3.py`: Create a temporary file under `./temp` and clean it up.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Files in current directory (first 5): ['README.md', 'LICENSE', ...]
Found 3 .py files under .
Created temporary file: /temp/tmp_abc123.txt
```

## Explanation
- **File system operations**: Use `pathlib.Path` for modern path handling.
- **Listing**: `Path.iterdir()` and `os.listdir()` show directory contents.
- **Walking**: Recursively traverse using `Path.rglob()` or `os.walk()`.
- **Temporary files**: Use `/temp` for transient artifacts to avoid polluting repo.
- **Best Practice**: Avoid hardcoding paths; check `Path.exists()` and handle permissions.
