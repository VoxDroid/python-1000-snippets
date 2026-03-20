# Game AI Implementation

## Description
This snippet demonstrates simple game AI behaviors using pure Python (no external libraries required).

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample2.py`)
```
X moves to 0
['X', '', '']
['', '', '']
['', '', '']
...
Result: draw
```

## Explanation
- **sample1.py**: Moves an agent toward a goal on a grid while avoiding obstacles.
- **sample2.py**: Uses minimax to play perfect Tic-Tac-Toe.
- **sample3.py**: Demonstrates a chasing enemy moving toward a player on a grid.
- **Best Practice**: Add randomness for non-deterministic behavior, and limit search depth for complex games.
