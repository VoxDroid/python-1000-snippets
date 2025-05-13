# Supply Chain Optimization

## Description
This snippet demonstrates optimizing supply chain costs using linear programming.

## Code
```python
# Note: Requires `scipy`. Install with `pip install scipy`
try:
    from scipy.optimize import linprog
    c = [2, 3]  # Costs
    A = [[-1, -1]]  # Constraints
    b = [-10]
    bounds = [(0, None), (0, None)]
    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds)
    print("Optimal quantities:", result.x.round(2))
except ImportError:
    print("Mock Output: Optimal quantities: [10.  0.]")
```

## Output
```
Mock Output: Optimal quantities: [10.  0.]
```
*(Real output with `scipy`: `Optimal quantities: [10.  0.]`)*

## Explanation
- **Supply Chain Optimization**: Minimizes costs subject to constraints.
- **Logic**: Solves a linear program for supply quantities.
- **Complexity**: O(n^3) for n variables in worst case.
- **Use Case**: Used in logistics and inventory management.
- **Best Practice**: Validate constraints; scale for large problems; test solutions.