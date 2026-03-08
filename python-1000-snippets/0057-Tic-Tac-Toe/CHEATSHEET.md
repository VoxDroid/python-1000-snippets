# Tic Tac Toe Cheatsheet

## Board setup
```python
board = [[' ']*3 for _ in range(3)]
```

## Print function
```
def print_board():
    for r in board:
        print('|'.join(r))
        print('-----')
```

## Win check
```
def check_win(p):
    # rows, cols, diagonals
```

## Tips
- Use loops to evaluate rows and columns.
- Use `all()` for concise win logic.
- Represent players as `'X'` and `'O'` strings.

## Running samples
Activate venv and pipe pairs of numbers (row col) to samples.
