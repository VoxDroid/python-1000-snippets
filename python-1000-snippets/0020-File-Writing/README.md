# File Writing

## Description
This snippet demonstrates how to write text to a file in Python using the `open()` function in write mode with the `with` statement.

## Code
```python
with open("output.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is a test.")
print("File written successfully.")
```

## Output
```
File written successfully.
```
*(Creates `output.txt` with:)*
```
Hello, Python!
This is a test.
```

## Explanation
- **File Writing**: `open("output.txt", "w")` opens (or creates) the file in write mode (`"w"`), overwriting existing content.
- **Write Method**: `file.write()` writes a string to the file. `\n` adds a newline.
- **With Statement**: Ensures the file is closed after writing.
- **Use Case**: File writing is used for saving logs, user data, or generating reports.
- **Best Practice**: Use `"a"` mode instead of `"w"` to append instead of overwrite; handle errors for disk issues.
## Additional Files
- `CHEATSHEET.md` describes modes (`w`, `a`, `x`, `wb`) and common `write` patterns.
- `SAMPLES/` includes:
  1. `sample1.py` – write multiple lines to a file.
  2. `sample2.py` – append to an existing file.
  3. `sample3.py` – write CSV-like data using `join`.

Run the samples under a `.venv` and inspect `output.txt` after execution.