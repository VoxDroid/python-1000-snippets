# Command Line Arguments Cheatsheet

## sys.argv
- `argv[0]` script name, `argv[1:]` parameters.
- Use `len(argv)` to check presence.

## argparse example
```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--count', type=int, default=1)
args = parser.parse_args()
```

## Tips
- For simple scripts, `sys.argv` suffices.
- Avoid manual parsing for flags; prefer `argparse` or `click`.

## Running samples
Activate venv and execute samples with arguments: `python sample2.py 1 2 3`.
