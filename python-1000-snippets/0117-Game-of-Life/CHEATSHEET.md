# 0117-Game-of-Life Cheatsheet

- **Purpose**: simulate Conway’s Game of Life on a 2D grid.
- **Function**: `game_of_life(board, steps)` returns the board after `steps` generations.
- **Board format**: list of lists with 0 (dead) or 1 (alive).

```python
from game_of_life import game_of_life

# simple block (still life)
board = [[1,1],[1,1]]
print(game_of_life(board, 5))

# glider pattern
board = [[0,1,0],[0,0,1],[1,1,1]]
print(game_of_life(board, 4))
```

- Patterns:
  * still life: block, beehive
  * oscillator: blinker (period 2)
  * spaceship: glider
- For large boards, consider using NumPy arrays or optimized neighbor counting.
- Visualize with `matplotlib.imshow` or a GUI toolkit.

