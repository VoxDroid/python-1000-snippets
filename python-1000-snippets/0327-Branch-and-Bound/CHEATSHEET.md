# 0327-Branch-and-Bound Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Knapsack branch-and-bound
python SAMPLES/sample2.py  # Subset sum branch-and-bound
python SAMPLES/sample3.py  # TSP branch-and-bound
```

## Tips
- Branch-and-bound explores a search tree of partial solutions.
- Use a **bound** to estimate best possible outcome below a branch.
- If the bound is worse than the best known solution, prune the branch.
- Use priority queues (best-first) for better performance.

## Common patterns
- Maintain a global best solution.
- Use recursion or an explicit stack to traverse branches.
- Compute an upper bound based on remaining resources.

## Example outline (knapsack bound)
```python
bound = current_value + greedy_fractional_value(remaining_items)
if bound <= best_value:
    return  # prune
```
