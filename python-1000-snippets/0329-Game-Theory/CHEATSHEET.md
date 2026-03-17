# 0329-Game-Theory Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Find pure strategy Nash equilibria
python SAMPLES/sample2.py  # Repeated Prisoner's Dilemma simulation
python SAMPLES/sample3.py  # Compute minimax value for zero-sum game
```

## Tips
- Represent games using payoff matrices (row player, column player).
- A pure-strategy Nash equilibrium is a pair of strategies where neither player can improve by switching unilaterally.
- In zero-sum games, the row player's maximin equals the column player's minimax.

## Common patterns
- Loop over all strategy profiles and check best responses.
- For repeated games, accumulate payoffs over rounds.
- Use linear programming for mixed-strategy equilibria (not shown here).

## Example outline (best response check)
```python
row_best = max(payoffs_row[i])
col_best = min(payoffs_col[:, j])
# check if (i, j) is a Nash equilibrium
```
