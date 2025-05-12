# Particle Swarm Simulation

## Description
This snippet demonstrates particle swarm optimization using `pyswarm`.

## Code
```python
# Note: Requires `pyswarm`. Install with `pip install pyswarm`
try:
    from pyswarm import pso
    def objective(x):
        return x[0]**2 + x[1]**2
    lb = [-10, -10]
    ub = [10, 10]
    xopt, fopt = pso(objective, lb, ub, swarmsize=10, maxiter=10)
    print("Optimal value:", fopt)
except ImportError:
    print("Mock Output: Optimal value: 0.0")
```

## Output
```
Mock Output: Optimal value: 0.0
```
*(Real output with `pyswarm`: `Optimal value: <near 0.0>`)*

## Explanation
- **Particle Swarm Simulation**: Optimizes a function using PSO.
- **Logic**: Minimizes a quadratic function with particle swarm.
- **Complexity**: O(n * i) for n particles, i iterations.
- **Use Case**: Used in optimization problems like ML tuning.
- **Best Practice**: Tune swarm size; set bounds; validate convergence.