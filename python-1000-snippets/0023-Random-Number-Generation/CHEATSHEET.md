# Random Number Generation Cheatsheet

## Import
```python
import random
```

## Common functions
- `random.randint(a,b)` integer inclusive
- `random.uniform(a,b)` float
- `random.choice(seq)` random element
- `random.shuffle(list)` shuffle in place

## Seeding
```python
random.seed(42)
```

## Tips
- Use `random.sample()` for unique choices.
- `random.random()` returns float in [0.0,1.0).

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

