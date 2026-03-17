# Nash Equilibrium

## Description
This snippet demonstrates finding Nash equilibria in simple 2-player games.

## Files
- `SAMPLES/sample1.py`: Find pure-strategy Nash equilibria in a normal-form game.
- `SAMPLES/sample2.py`: Compute mixed-strategy Nash equilibrium in a 2x2 zero-sum game.
- `SAMPLES/sample3.py`: Compute mixed-strategy Nash equilibrium for a general 2x2 game.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Expected output (example)
```
Pure Nash equilibria: [(0, 0)]
Mixed strategy (row): 0.25, (col): 0.75
General 2x2 mixed equilibrium: row=(0.5,0.5), col=(0.5,0.5)
```

## Explanation
- **Nash equilibrium**: No player can gain by unilaterally deviating.
- **Pure strategy equilibrium**: Players choose a single action with probability 1.
- **Mixed strategy equilibrium**: Players randomize; payoffs are equalized across support.
