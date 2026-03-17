# 0330-Nash-Equilibrium Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Pure strategy equilibrium
python SAMPLES/sample2.py  # Mixed strategy (zero-sum)
python SAMPLES/sample3.py  # Mixed strategy (general 2x2)
```

## Tips
- A (pure strategy) Nash equilibrium is a profile where no player can improve by changing their strategy alone.
- For 2x2 zero-sum games, the mixed-strategy equilibrium can be computed analytically.
- In general, solve for probabilities that make opponents indifferent between their strategies.

## Common formulas (2x2 zero-sum)
Given payoff matrix for row player:
```
[a b]
[c d]
```
Row mixes p on top row, column mixes q on left column.
- p = (d - c) / (a - b - c + d)
- q = (d - b) / (a - b - c + d)
