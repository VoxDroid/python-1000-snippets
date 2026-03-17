# 0328-Constraint-Satisfaction Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Map coloring
python SAMPLES/sample2.py  # 4x4 Sudoku solver
python SAMPLES/sample3.py  # Alphametic puzzle (SEND+MORE=MONEY)
```

## Tips
- Model the problem with variables, domains, and constraints.
- Use backtracking to assign variables and undo assignments when constraints fail.
- Add simple constraint checks early (e.g., all-different, row/column constraints) to prune search.

## Common patterns
- Track a dictionary of variable assignments.
- Use recursive search and a `is_valid` function to check constraints.
- Optionally apply forward checking or arc consistency to reduce domains.

## Example outline (all-different check)
```python
if value in assigned.values():
    return False
```
