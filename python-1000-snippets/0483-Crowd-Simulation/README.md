# Crowd Simulation

## Description
This snippet demonstrates a simple crowd simulation using pure Python.

## Code
The sample scripts show:
- `sample1.py`: Random-walk agent positions and simple update.
- `sample2.py`: Crowd density in a 2D grid.
- `sample3.py`: Attraction/repulsion step mechanics.

## Output
`sample1.py` prints initial/after-step positions for agents.

`sample2.py` prints density stats (`grid[0][0]` and total agents).

`sample3.py` prints final positions after attraction/repulsion dynamics.

## Explanation
- **Crowd Simulation**: Simulates agent movement and density logic.
- **Logic**: Random walk updates, grid density mapping, attraction/repulsion.
- **Complexity**: O(n*t) for n agents over t steps.
- **Use Case**: Used in traffic/crowd modeling and behavior experiments.
- **Best Practice**: Add collision avoidance, boundary handling, realistic rules.
