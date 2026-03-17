# Branch and Bound

## Description
This snippet demonstrates branch-and-bound search: systematically explore branches while pruning those that cannot yield better solutions.

## Files
- `SAMPLES/sample1.py`: 0/1 knapsack solved via branch-and-bound.
- `SAMPLES/sample2.py`: Subset sum with bounding.
- `SAMPLES/sample3.py`: Simple TSP using branch-and-bound pruning.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Expected output (example)
```
Best knapsack value: 22
Subset sum target 9: True
Best TSP tour length: 9
```

## Explanation
- **Branch and bound**: Enumerate possible partial solutions (branches) and use bounds to prune unpromising branches.
- **Bounding function**: Provides optimistic estimate of best possible value under a branch.
- **Use Case**: Solving combinatorial optimization problems with pruning.
