# Dice Roller Cheatsheet

## Rolling dice
```python
import random
random.randint(1, sides)
```

## Function
```
def roll_dice(sides, rolls):
    return [random.randint(1, sides) for _ in range(rolls)]
```

## Tips
- Use `random.seed()` to make tests repeatable.
- Use `collections.Counter` to tally outcomes.
- Validate that `sides` and `rolls` are positive integers.

## Example usage
```
print(roll_dice(6, 3))
```

## Running samples
Activate virtual env and run `SAMPLES/sample*.py`.
