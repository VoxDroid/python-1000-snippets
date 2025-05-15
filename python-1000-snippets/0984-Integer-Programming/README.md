# Integer Programming

## Description
This snippet implements integer programming for a supply chain company, optimizing warehouse allocation to minimize shipping costs.

## Code
```python
# Integer Programming: Warehouse allocation
# Note: Requires `pulp` and `numpy`. Install with `pip install pulp numpy`
try:
    from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, LpStatus
    import numpy as np
    
    # Integer programming model
    def warehouse_allocation(n_warehouses: int, n_customers: int, costs: np.ndarray, supplies: np.ndarray, demands: np.ndarray) -> dict:
        # Define ILP problem
        prob = LpProblem("Warehouse_Allocation", LpMinimize)
        
        # Decision variables: x[i,j] = 1 if warehouse i serves customer j
        x = [[LpVariable(f"x_{i}_{j}", cat=LpBinary) for j in range(n_customers)] for i in range(n_warehouses)]
        
        # Objective: Minimize shipping costs
        prob += lpSum(costs[i, j] * x[i][j] for i in range(n_warehouses) for j in range(n_customers))
        
        # Constraints
        # Each customer is served by exactly one warehouse
        for j in range(n_customers):
            prob += lpSum(x[i][j] for i in range(n_warehouses)) == 1
        # Warehouse supply constraints
        for i in range(n_warehouses):
            prob += lpSum(x[i][j] * demands[j] for j in range(n_customers)) <= supplies[i]
        
        # Solve problem
        prob.solve()
        status = LpStatus[prob.status]
        if status == "Optimal":
            allocation = [[x[i][j].varValue for j in range(n_customers)] for i in range(n_warehouses)]
            return {'status': status, 'allocation': allocation, 'cost': prob.objective.value()}
        return {'status': status, 'allocation': None, 'cost': None}

    # Run ILP simulation
    def run_warehouse_allocation(n_warehouses: int, n_customers: int) -> dict:
        # Optimize warehouse allocation
        costs = np.random.uniform(10, 100, (n_warehouses, n_customers))  # Shipping costs
        supplies = np.random.randint(50, 200, n_warehouses)  # Warehouse supplies
        demands = np.random.randint(10, 50, n_customers)     # Customer demands
        return warehouse_allocation(n_warehouses, n_customers, costs, supplies, demands)

    # Example usage
    result = run_warehouse_allocation(n_warehouses=3, n_customers=5)
    print("Integer programming result:", result['cost'])  # Total cost
except ImportError:
    print("Mock Output: Integer programming result: 250.0")
```

## Output
```
Mock Output: Integer programming result: 250.0
```
*(Real output with `pulp`: `Integer programming result: <total cost, e.g., 250.0>`)*

## Explanation
- **Purpose**: Optimizes warehouse allocation using integer programming.
- **Real-World Use Case**: A supply chain company uses this to minimize shipping costs, improving logistics.
- **Code Breakdown**:
  - The `warehouse_allocation` function defines an ILP with binary variables.
  - Constraints ensure each customer is served and supplies are not exceeded.
  - The `run_warehouse_allocation` function returns the optimal allocation and cost.
- **Technical Challenges**: Handling large instances, ensuring feasibility, and modeling complex constraints.
- **Integration**: Complements Linear Programming (Snippet 985) for optimization.
- **Scalability**: Polynomial with LP solvers; large problems require branch-and-cut.
- **Performance Metrics**: Solves small instances (<10 warehouses) in seconds.
- **Best Practices**: Use real cost data, validate with logistics models, and add capacity constraints.
- **Extensions**: Include fixed costs or multi-period planning.
- **Limitations**: Simplified model; real logistics involve dynamic demands.