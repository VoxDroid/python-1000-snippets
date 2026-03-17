# Integer Programming

## Description
This snippet implements integer programming heuristics in pure Python (no external solvers).

## Files
- `SAMPLES/sample1.py`: Simple integer knapsack via brute-force search.
- `SAMPLES/sample2.py`: Integer linear programming via branch-and-bound for small cases.
- `SAMPLES/sample3.py`: Simple preset scheduling problem solved via enumeration.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Best knapsack value: 7, items: [1, 1, 0, 1]
Best solution: [2, 0, 1], value: 8
Best schedule value: 5, assignment: [0, 1, 0]
```

## Explanation
- **Integer programming**: Optimizes an objective with integer decision variables.
- **Brute-force/branch-and-bound**: Typical for small problem sizes; scales poorly.
- **Use Case**: Knapsack, scheduling, resource allocation with discrete decisions.
