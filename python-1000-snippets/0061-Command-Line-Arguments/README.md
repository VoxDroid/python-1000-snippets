# Command Line Arguments

## Description
This snippet demonstrates how to access command-line arguments in Python using the `sys.argv` list.

## Code
```python
import sys

print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
```

## Output
*(Run as `python script.py arg1 arg2`):*
```
Script name: script.py
Arguments: ['arg1', 'arg2']
```

## Explanation
- **sys.argv**: A list where `sys.argv[0]` is the script name, and `sys.argv[1:]` are the arguments passed.
- **Use Case**: Command-line arguments are used for scripts that accept user inputs, like file names or options.
- **Error Handling**: Check `len(sys.argv)` to ensure required arguments are provided.
- **Best Practice**: Use `argparse` for complex argument parsing in production scripts.

## Additional Files
- `CHEATSHEET.md` contrasts `sys.argv` vs `argparse` and shows examples.
- `SAMPLES/` includes:
  1. `sample1.py` – echo the script name and arguments.
  2. `sample2.py` – sum integer arguments provided on command line.
  3. `sample3.py` – use `argparse` to parse options like `--count`.

Run samples under `.venv`; provide arguments directly when executing.