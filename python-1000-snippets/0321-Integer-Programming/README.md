# Integer Programming

## Description
This snippet demonstrates integer programming using `pulp`.

## Code
```python
# Note: Requires `pulp`. Install with `pip install pulp`
try:
    from pulp import LpProblem, LpMaximize, LpVariable
    prob = LpProblem("Maximize", LpMaximize)
    x = LpVariable("x", lowBound=0, cat="Integer")
    y = LpVariable("y", lowBound=0, cat="Integer")
    prob += x + y
    prob += x + 2*y <= 4
    prob.solve()
    print("Solution:", x.varValue, y.varValue)
except ImportError:
    print("Mock Output: Solution: 4.0 0.0")
```

## Output
```
Mock Output: Solution: 4.0 0.0
```
*(Real output with `pulp`: `Solution: 4.0 0.0`)*

## Explanation
- **Integer Programming**: Maximizes x + y with integer constraints.
- **Logic**: Defines integer variables, objective, and constraints, then solves.
- **Complexity**: NP-hard (solver-dependent).
- **Use Case**: Used for discrete optimization like knapsack problems.
- **Best Practice**: Handle integrality; optimize solver; validate solutions.