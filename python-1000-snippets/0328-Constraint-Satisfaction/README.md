# Constraint Satisfaction

## Description
This snippet demonstrates constraint satisfaction using `python-constraint`.

## Code
```python
# Note: Requires `python-constraint`. Install with `pip install python-constraint`
try:
    from constraint import Problem
    problem = Problem()
    problem.addVariable("x", [1, 2])
    problem.addVariable("y", [1, 2])
    problem.addConstraint(lambda x, y: x + y == 3)
    solutions = problem.getSolutions()
    print("Solutions:", solutions)
except ImportError:
    print("Mock Output: Solutions: [{'x': 2, 'y': 1}, {'x': 1, 'y': 2}]")
```

## Output
```
Mock Output: Solutions: [{'x': 2, 'y': 1}, {'x': 1, 'y': 2}]
```
*(Real output with `python-constraint`: `Solutions: [{'x': 2, 'y': 1}, {'x': 1, 'y': 2}]`)*

## Explanation
- **Constraint Satisfaction**: Solves x + y = 3 with discrete variables.
- **Logic**: Defines variables and constraints, then finds solutions.
- **Complexity**: O(d^n) for d domain size, n variables (solver-dependent).
- **Use Case**: Used for scheduling or puzzles.
- **Best Practice**: Reduce domains; use efficient constraints; validate solutions.