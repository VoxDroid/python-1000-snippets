# File System Operations

## Description
This snippet demonstrates file system operations using `os` to list directory contents.

## Code
```python
import os
try:
    files = os.listdir(".")
    print("Files:", files[:3])  # Show up to 3 for brevity
except FileNotFoundError:
    print("Mock Output: Files: ['file1.txt', 'file2.py', 'folder']")
```

## Output
```
Mock Output: Files: ['file1.txt', 'file2.py', 'folder']
```
*(Real output with `os`: `Files: [<actual files in directory>]`)*

## Explanation
- **File System Operations**: Lists files in the current directory.
- **Logic**: Uses `os.listdir` to retrieve file names.
- **Complexity**: O(n) for n files.
- **Use Case**: Used for file management or automation.
- **Best Practice**: Handle permissions; validate paths; use `pathlib` for modern code.