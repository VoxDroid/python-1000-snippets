# Branch Coverage Analysis

## Description
This snippet demonstrates how to write code that can be measured for **branch coverage** and how to use the `coverage` package to collect branch coverage data.

## Files
- `SAMPLES/sample1.py` — Minimal branchy logic.
- `SAMPLES/sample2.py` — Programmatic branch coverage run with console report.
- `SAMPLES/sample3.py` — Programmatic branch coverage run with HTML report output.

## Usage
### 1) Run the core logic
```bash
python SAMPLES/sample1.py
```

### 2) Run a branch coverage report (requires `coverage`)
```bash
python SAMPLES/sample2.py
```

### 3) Generate an HTML branch coverage report
```bash
python SAMPLES/sample3.py
```

## Output
- If `coverage` is not installed, the scripts will print a helpful installation message.
- When `coverage` is installed, `sample2.py` prints a summary report with branch coverage information.
- When `coverage` is installed, `sample3.py` prints a filesystem path to an HTML report.

## Notes
- Install coverage with:
  ```bash
  pip install coverage
  ```
- Alternative direct CLI usage:
  ```bash
  coverage run --branch -m pytest
  coverage report -m
  coverage html
  ```
- Branch coverage is useful to ensure all decision points (if/else, loops, exception handlers) are exercised by tests.
