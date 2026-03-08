# Number Guessing Game Cheatsheet

## Generating secret
```python
import random
secret = random.randint(1, 100)
```
- Seed with `random.seed(n)` for reproducibility.

## Main loop
```python
while True:
    guess = int(input())
    if guess == secret: break
```

## Tips
- Use `try/except` to handle non-integers.
- Add `attempts` counter, break on max tries.

## Running samples
Activate venv and run `SAMPLES/sample*.py`; pipe guesses to avoid manual entry.
