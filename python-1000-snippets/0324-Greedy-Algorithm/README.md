# Greedy Algorithm

## Description
This snippet demonstrates greedy algorithms, where local optimal choices lead to a global solution.

## Files
- `SAMPLES/sample1.py`: Coin change using a greedy heuristic.
- `SAMPLES/sample2.py`: Interval scheduling (activity selection).
- `SAMPLES/sample3.py`: Fractional knapsack (continuous version).

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Expected output (example)
```
Change for 67: [25, 25, 10, 5, 1, 1]
Selected intervals: [(1, 3), (3, 5), (5, 7)]
Fractional knapsack value: 240.0
```

## Explanation
- **Greedy algorithm**: Builds a solution by repeatedly choosing the best local option.
- **Use Case**: Common in scheduling, optimization, and approximation algorithms.
- **Best Practice**: Verify that greedy choice property holds; not all problems are greedy-solvable.
