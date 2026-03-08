# File Copy

## Description
This snippet copies the contents of one file to another using the `shutil` module, preserving the original file.

## Code
```python
import shutil

try:
    shutil.copy("source.txt", "destination.txt")
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")
except IOError:
    print("Error during file copy.")
```

## Output
*(Assuming `source.txt` exists):*
```
File copied successfully.
```
*(If `source.txt` doesn't exist):*
```
Source file not found.
```

## Explanation
- **shutil.copy()**: Copies the content and metadata of `source.txt` to `destination.txt`.
- **Error Handling**: Catches `FileNotFoundError` for missing files and `IOError` for other issues.
- **Use Case**: File copying is used in backups, file management, or data processing.
- **Alternative**: Use `shutil.copyfile()` for content-only copying without metadata.
- **Best Practice**: Validate file paths and permissions before copying.

## Additional Files
- `CHEATSHEET.md` compares `shutil.copy`, `copyfile`, `copy2`, and `move`.
- `SAMPLES/` includes:
  1. `sample1.py` – create a source file and copy it.
  2. `sample2.py` – copy multiple files listed in a directory.
  3. `sample3.py` – copy and then rename the destination.

Run samples in a `.venv`; they write files in the snippet directory and clean up as needed.