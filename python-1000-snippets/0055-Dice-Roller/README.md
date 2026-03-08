# Dice Roller

## Description
This snippet simulates rolling dice with a specified number of sides, using the `random` module to generate random numbers.

## Code
```python
import random

def roll_dice(sides, rolls):
    return [random.randint(1, sides) for _ in range(rolls)]

sides = int(input("Enter number of sides: "))
rolls = int(input("Enter number of rolls: "))
results = roll_dice(sides, rolls)
print("Results:", results)
```

## Output
```
Enter number of sides: 6
Enter number of rolls: 3
Results: [4, 1, 6]
```
*(Output varies each run)*

## Explanation
- **Dice Logic**: `random.randint(1, sides)` generates a random number for each roll.
- **Function**: `roll_dice(sides, rolls)` returns a list of roll results.
- **List Comprehension**: Efficiently generates multiple rolls.
- **Use Case**: Dice rollers are used in games, simulations, or random sampling.
- **Best Practice**: Validate inputs (e.g., positive integers) and handle edge cases.

## Additional Files
- `CHEATSHEET.md` shows how to roll different dice and aggregate results.
- `SAMPLES/` contains:
  1. `sample1.py` – roll a standard six‑sided die multiple times.
  2. `sample2.py` – roll a custom-sided die and tally frequency.
  3. `sample3.py` – simulate a dice game comparing two players.

Run the samples in a `.venv`; use `printf` to supply input automatically.