# 0326-Backtracking Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Permutations
python SAMPLES/sample2.py  # N-Queens
python SAMPLES/sample3.py  # Subset sum
```

## Tips
- Backtracking builds solutions step-by-step and backtracks on failure.
- Use recursion and maintain a partial solution state.
- Prune early by checking constraints at each step.

## Common patterns
- Generate permutations/combinations recursively.
- Solve puzzles (N-Queens, Sudoku) by placing one element at a time.
- Use helper functions to check validity and restore state on backtracking.

## Example outline (permutations)
```python
if len(curr) == len(nums):
    results.append(list(curr))
    return
for x in nums:
    if x not in curr:
        curr.append(x)
        backtrack()
        curr.pop()
```
