# Hangman Game Cheatsheet

## Core elements
- `word`: secret string
- `display`: list of chars or `_` for unrevealed letters
- `guessed`: set of guessed letters
- `mistakes` vs `max_mistakes`

## Display update
```python
for i,l in enumerate(word):
    if l==guess: display[i]=guess
```

## Tips
- Use `random.choice` to pick word; seed for tests.
- Check repeated guesses with set membership.
- To support multi-letter guesses, adjust logic accordingly.

## Running samples
Activate venv and pipe guesses to files in `SAMPLES/`.
