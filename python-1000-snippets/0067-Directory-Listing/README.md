# Directory Listing

## Description
This snippet lists all files and directories in a specified directory using the `os` module.

## Code
```python
import os

dirname = "."
try:
    contents = os.listdir(dirname)
    print("Directory contents:", contents)
except FileNotFoundError:
    print("Directory not found.")
except OSError:
    print("Error listing directory.")
```

## Output
*(Assuming current directory has `file1.txt` and `folder1`):*
```
Directory contents: ['file1.txt', 'folder1']
```

## Explanation
- **os.listdir()**: Returns a list of names of files and directories in the specified path (`.` for current directory).
- **Error Handling**: Catches `FileNotFoundError` for invalid paths and `OSError` for permission issues.
- **Use Case**: Directory listing is used in file explorers, backups, or file processing scripts.
- **Flexibility**: Combine with `os.path` to filter files or directories.
- **Best Practice**: Specify absolute paths for clarity and handle large directories efficiently.