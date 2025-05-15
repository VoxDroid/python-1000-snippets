# Linear Programming

## Description
This snippet implements linear programming for a farming cooperative, optimizing crop production to maximize profit.

## Code
```python
# Linear Programming: Crop production optimization
# Note: Requires `pulp` and `numpy`. Install with `pip install pulp numpy`
try:
    from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus
    import numpy as np
    
    # Linear programming model
    def crop_optimization(n_crops: int, land: float, water: float, profits: np.ndarray, land_use: np.ndarray, water_use: np.ndarray) -> dict:
        # Define LP problem
        prob = LpProblem("Crop_Optimization", LpMaximize)
        
        # Decision variables: acres for each crop
        x = [LpVariable(f"x_{i}", lowBound=0) for i in range(n_crops)]
        
        # Objective: Maximize profit
        prob += lpSum(profits[i] * x[i] for i in range(n_crops))
        
        # Constraints
        prob += lpSum(land_use[i] * x[i] for i in range(n_crops)) <= land  # Land constraint
        prob += lpSum(water_use[i] * x[i] for i in range(n_crops)) <= water  # Water constraint
        
        # Solve problem
        prob.solve()
        status = LpStatus[prob.status]
        if status == "Optimal":
            allocation = [x[i].varValue for i in range(n_crops)]
            return {'status': status, 'allocation': allocation, 'profit': prob.objective.value()}
        return {'status': status, 'allocation': None, 'profit': None}

    # Run LP simulation
    def run_crop_optimization(n_crops: int) -> dict:
        # Optimize crop production
        profits = np.random.uniform(100, 500, n_crops)  # Profit per acre
        land_use = np.random.uniform(0.5, 2, n_crops)   # Acres per crop
        water_use = np.random.uniform(10, 50, n_crops)  # Water per crop
        return crop_optimization(n_crops, land=100, water=1000, profits=profits, land_use=land_use, water_use=water_use)

    # Example usage
    result = run_crop_optimization(n_crops=3)
    print("Linear programming result:", result['profit'])  # Total profit
except ImportError:
    print("Mock Output: Linear programming result: 15000.0")
```

## Output
```
Mock Output: Linear programming result: 15000.0
```
*(Real output with `pulp`: `Linear programming result: <total profit, e.g., 15000.0>`)*

## Explanation
- **Purpose**: Optimizes crop production using linear programming.
- **Real-World Use Case**: A farming cooperative uses this to maximize profits, improving resource allocation.
- **Code Breakdown**:
  - The `crop_optimization` function defines an LP with continuous variables.
  - Constraints limit land and water usage.
  - The `run_crop_optimization` function returns the optimal allocation and profit.
- **Technical Challenges**: Ensuring feasibility, handling large instances, and modeling uncertainty.
- **Integration**: Complements Integer Programming (Snippet 984) for optimization.
- **Scalability**: Polynomial with LP solvers; large problems require efficient solvers.
- **Performance Metrics**: Solves small instances (<10 crops) in milliseconds.
- **Best Practices**: Use real agricultural data, validate with farm records, and add labor constraints.
- **Extensions**: Include price variability or multi-season planning.
- **Limitations**: Linear model; real farming involves nonlinear effects.