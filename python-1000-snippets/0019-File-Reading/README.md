# File Reading

## Description
This snippet shows how to read text from a file in Python using the `open()` function and `with` statement, which ensures proper file handling.

## Code
```python
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print("File content:", content)
except FileNotFoundError:
    print("File not found.")
```

## Output
*(Assuming `example.txt` contains "Hello, World!")*
```
File content: Hello, World!
```
*(If `example.txt` doesn't exist)*
```
File not found.
```

## Explanation
- **File Reading**: `open("example.txt", "r")` opens the file in read mode (`"r"`).
- **With Statement**: Ensures the file is properly closed after reading, even if an error occurs.
- **Read Method**: `file.read()` reads the entire file content as a string.
- **Error Handling**: Catches `FileNotFoundError` if the file doesn't exist.
- **Use Case**: File reading is used for processing logs, configuration files, or user data.
- **Best Practice**: Always use `with` for file operations and handle potential errors.

## Additional Files
- `CHEATSHEET.md` lists common modes (`r`, `rb`, etc.) and read methods (`read`, `readline`, `readlines`).
- `SAMPLES/` includes:
  1. `sample1.py` – read entire file and print lines with numbers.
  2. `sample2.py` – read file line by line using a loop.
  3. `sample3.py` – count words in a file with error handling.

Prepare an `example.txt` or simulate it when running samples inside a `.venv`.