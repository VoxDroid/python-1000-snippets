# File Delete

## Description
This snippet deletes a specified file using the `os` module, with error handling for missing files.

## Code
```python
import os

filename = "file_to_delete.txt"
try:
    os.remove(filename)
    print(f"File '{filename}' deleted successfully.")
except FileNotFoundError:
    print(f"File '{filename}' not found.")
except OSError:
    print("Error during file deletion.")
```

## Output
*(Assuming `file_to_delete.txt` exists):*
```
File 'file_to_delete.txt' deleted successfully.
```
*(If file doesn't exist):*
```
File 'file_to_delete.txt' not found.
```

## Explanation
- **os.remove()**: Deletes the specified file from the filesystem.
- **Error Handling**: Catches `FileNotFoundError` for missing files and `OSError` for permission issues.
- **Use Case**: File deletion is used in cleanup scripts or temporary file management.
- **Caution**: Deletion is permanent; ensure the correct file is targeted.
- **Best Practice**: Confirm file existence and user intent before deletion.