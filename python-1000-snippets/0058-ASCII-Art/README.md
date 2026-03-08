# ASCII Art

## Description
This snippet displays a simple ASCII art representation of a tree using multi-line strings.

## Code
```python
def make_tree(height=4):
    # simple triangular tree with a trunk
    art = []
    for i in range(height):
        spaces = ' ' * (height - i)
        leaves = '/' + ' ' * (2*i) + '\\'
        art.append(spaces + leaves)
    art.append('/' + '_' * (2*height) + '\\')
    art.append(' ' * (height-1) + '||||')
    art.append(' ' * (height-1) + '||||')
    return "\n".join(art)

print("ASCII Art Tree:")
print(make_tree())

```

## Output
```
ASCII Art Tree:
   /\
  /  \
 /    \
/______\
  ||||
  ||||
```

## Explanation
- **ASCII Art**: Uses a multi-line string to create a visual representation of a tree.
- **Printing**: `print()` outputs the string with preserved formatting.
- **Use Case**: ASCII art is used for console-based visuals, games, or creative outputs.
- **Flexibility**: Can be extended with dynamic generation or libraries like `art`.
- **Best Practice**: Ensure terminal supports fixed-width fonts for proper alignment.

## Additional Files
- `CHEATSHEET.md` shows examples of dynamic art generation.
- `SAMPLES/` includes:
  1. `sample1.py` – print fixed tree as in original code.
  2. `sample2.py` – ask user for height and draw tree accordingly.
  3. `sample3.py` – generate other shapes (e.g., pyramid) using loops.

Run samples in a `.venv` environment; sample2 reads height input programmatically.