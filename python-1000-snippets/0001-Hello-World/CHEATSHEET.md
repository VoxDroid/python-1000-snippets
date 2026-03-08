# Hello World Cheatsheet

This cheatsheet explains the basics of printing output in Python and provides quick-start instructions.

## Running the Snippet

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Navigate to the snippet directory:
   ```bash
   cd python-1000-snippets/0001-Hello-World
   ```
3. Execute any sample file with:
   ```bash
   python sample1.py
   ```

## Key Points

- `print()` is the built-in function for displaying text to the console.
- Strings must be enclosed in quotes (`"` or `'`).
- Python automatically adds a newline after each `print()` call. Use `end=''` to change this.

## Examples

```python
print("Hello, World!")           # simple message
print('Value:', 42)               # multiple arguments are separated by spaces
print("No newline", end="")    # modify ending behavior
```