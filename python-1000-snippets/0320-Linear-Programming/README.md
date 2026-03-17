# Linear Programming

## Description
This snippet provides pure-Python examples of solving linear programming (LP) problems using the simplex method without external dependencies.

## Files
- `SAMPLES/sample1.py`: Maximize a linear objective with two variables and constraints.
- `SAMPLES/sample2.py`: Solve a small diet problem (minimize cost subject to nutritional constraints).
- `SAMPLES/sample3.py`: Solve an LP with both equality and inequality constraints.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Solution: x=1.33, y=1.33, objective=2.67
Solution: x=0.00, y=2.00, objective=3.00
Solution: x=2.00, y=0.00, objective=6.00
```

## Explanation
- **Simplex**: Iteratively improves a basic feasible solution to optimize the objective.
- **Feasible region**: Defined by linear constraints; optimal solution is at a vertex.
- **Use Case**: Resource allocation, diet planning, production planning.
