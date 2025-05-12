# Linear Programming

## Description
This snippet demonstrates linear programming using `pulp`.

## Code
```python
# Note: Requires `pulp`. Install with `pip install pulp`
try:
    from pulp import LpProblem, LpMaximize, LpVariable
    prob = LpProblem("Maximize", LpMaximize)
    x = LpVariable("x", lowBound=0)
    y = LpVariable("y", lowBound=0)
    prob += x + y
    prob += x + 2*y <= 4
    prob += 2*x + y <= 4
    prob.solve()
    print("Solution:", x.varValue, y.varValue)
except ImportError:
    print("Mock Output: Solution: 1.3333333 1.3333333")
```

## Output
```
Mock Output: Solution: 1.3333333 1.3333333
```
*(Real output with `pulp`: `Solution: 1.3333333 1.3333333`)*

## Explanation
- **Linear Programming**: Maximizes x + y subject to linear constraints.
- **Logic**: Defines variables, objective, and constraints, then solves.
- **Complexity**: O(n) for n variables (solver-dependent).
- **Use Case**: Used for resource allocation or scheduling.
- **Best Practice**: Validate constraints; handle unbounded cases; check feasibility.