# Particle Swarm Simulation

## Description
This snippet demonstrates particle swarm optimization with a pure Python implementation.

## Code
The sample scripts show:
- `sample1.py`: Minimize x^2 + y^2 and print the best point.
- `sample2.py`: Track convergence history of a shifted quadratic objective.
- `sample3.py`: Optimize the Rosenbrock function and print the best solution.

## Output
`sample1.py` prints a best point and value near zero for f(x,y)=x^2+y^2.
`sample2.py` prints convergence history for a shifted quadratic objective.
`sample3.py` prints Rosenbrock optimization results.

## Explanation
- **Particle Swarm Simulation**: Optimizes functions using a swarm of candidate solutions.
- **Logic**: Each particle updates velocity and position from personal and global best values.
- **Complexity**: O(n * i) for n particles, i iterations.
- **Use Case**: Useful for global optimization problems and parameter search.
- **Best Practice**: Tune swarm size, inertia, and acceleration constants for stability.
