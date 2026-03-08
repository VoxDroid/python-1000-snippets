# Directory Creation

## Description
This snippet creates a new directory using the `os` module, with error handling for existing directories.

## Code
```python
import os

dirname = "new_folder"
try:
    os.mkdir(dirname)
    print(f"Directory '{dirname}' created successfully.")
except FileExistsError:
    print(f"Directory '{dirname}' already exists.")
except OSError:
    print("Error creating directory.")
```

## Output
*(If directory doesn't exist):*
```
Directory 'new_folder' created successfully.
```
*(If directory exists):*
```
Directory 'new_folder' already exists.
```

## Explanation
- **os.mkdir()**: Creates a single directory with the specified name.
- **Error Handling**: Catches `FileExistsError` for existing directories and `OSError` for other issues.
- **Use Case**: Directory creation is used in file organization, project setup, or data storage.
- **Alternative**: Use `os.makedirs()` for creating nested directories.
- **Best Practice**: Validate directory names and permissions before creation.

## Additional Files
- `CHEATSHEET.md` describes `os.mkdir`, `os.makedirs`, `pathlib.Path.mkdir`, and existence checks.
- `SAMPLES/` contains:
  1. `sample1.py` – create a single directory.
  2. `sample2.py` – make nested directories with `makedirs`.
  3. `sample3.py` – prompt for a directory name and create it if absent.

Run samples in a `.venv`; sample3 reads input by pipe for testing.