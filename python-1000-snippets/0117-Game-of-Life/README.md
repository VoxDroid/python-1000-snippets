# Game of Life

## Description
This snippet implements Conway’s Game of Life, a cellular automaton where cells live, die, or reproduce based on neighbor counts.

## Code
```python
def game_of_life(board, steps):
    def count_neighbors(board, i, j):
        count = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    count += board[ni][nj]
        return count

    for _ in range(steps):
        new_board = [[0] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors = count_neighbors(board, i, j)
                if board[i][j] == 1 and neighbors in [2, 3]:
                    new_board[i][j] = 1
                elif board[i][j] == 0 and neighbors == 3:
                    new_board[i][j] = 1
        board = new_board
    return board

board = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
result = game_of_life(board, 1)
for row in result:
    print(row)
```

## Output
```
[0, 0, 0]
[1, 0, 1]
[0, 1, 1]
```

## Explanation
- **Game of Life**: A cell survives with 2-3 live neighbors, dies otherwise; a dead cell with 3 live neighbors becomes alive.
- **Logic**: Computes neighbor counts and applies rules for each generation.
- **Complexity**: O(rows * cols * steps) time.
- **Use Case**: Used in computational biology or simulation studies.
- **Best Practice**: Optimize for large boards; visualize with graphics libraries.