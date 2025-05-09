# Tic Tac Toe

## Description
This snippet implements a Tic Tac Toe game for two players (X and O) on a 3x3 grid, checking for wins or draws.

## Code
```python
board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

player = "X"
moves = 0
while moves < 9:
    print_board()
    row = int(input(f"Player {player}, enter row (0-2): "))
    col = int(input(f"Player {player}, enter col (0-2): "))
    if board[row][col] == " ":
        board[row][col] = player
        moves += 1
        if check_win(player):
            print_board()
            print(f"Player {player} wins!")
            break
        player = "O" if player == "X" else "X"
    else:
        print("Cell taken!")
if moves == 9 and not check_win(player):
    print_board()
    print("It's a draw!")
```

## Output
```
 | | 
-----
 | | 
-----
 | | 
-----
Player X, enter row (0-2): 0
Player X, enter col (0-2): 0
X| | 
-----
 | | 
-----
 | | 
-----
Player O, enter row (0-2): 1
Player O, enter col (0-2): 1
...
X| | 
-----
 |O| 
-----
 | |X
-----
Player X wins!
```
*(Output varies based on moves)*

## Explanation
- **Game Logic**: Players alternate placing `X` or `O` on a 3x3 grid; checks for row, column, or diagonal wins.
- **Functions**: `print_board()` displays the grid; `check_win()` checks for a winner.
- **Use Case**: Demonstrates nested lists, conditionals, and game logic.
- **Error Handling**: Should validate input (e.g., range, integers) in production.
- **Best Practice**: Add a loop for replay and robust input validation.