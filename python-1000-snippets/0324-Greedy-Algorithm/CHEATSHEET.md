# 0324-Greedy-Algorithm Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Coin change
python SAMPLES/sample2.py  # Interval scheduling
python SAMPLES/sample3.py  # Fractional knapsack
```

## Tips
- Greedy algorithms make the locally optimal choice at each step.
- They work when the problem has the **greedy-choice property** and **optimal substructure**.
- Always verify correctness (counterexamples exist for many problems).

## Common patterns
- Sort items by a key (value/weight, end time, etc.)
- Iterate and make the best feasible choice
- Stop when you cannot improve the solution further

## Example outline (coin change)
```python
coins = [25, 10, 5, 1]
amount = 67
for coin in coins:
    while amount >= coin:
        # take coin
        amount -= coin
```
