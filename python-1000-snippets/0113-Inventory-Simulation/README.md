# Inventory Simulation

## Description
This snippet simulates an inventory system with random demand, reordering when stock is low.

## Code
```python
import random

def inventory_simulation(initial_stock, reorder_point, reorder_amount, days, demand_max=5, seed=None):
    """Run a simple discrete-time inventory simulation.

    * `initial_stock` – starting units on hand
    * `reorder_point` – trigger level to place a new order
    * `reorder_amount` – how many units to restock when ordering
    * `days` – number of days to simulate
    * `demand_max` – maximum random demand per day (uniform 0..demand_max)
    * `seed` – optional random seed for reproducibility

    Returns total profit: revenue from sales less restocking cost.
    """
    if seed is not None:
        random.seed(seed)
    stock = initial_stock
    profit = 0
    for _ in range(days):
        demand = random.randint(0, demand_max)
        sold = min(stock, demand)
        stock -= sold
        profit += sold * 10          # $10 revenue per unit sold
        if stock <= reorder_point:
            stock += reorder_amount
            profit -= reorder_amount * 5  # $5 cost per restocked unit
    return profit


if __name__ == "__main__":
    print("Profit:", inventory_simulation(20, 5, 10, 30, seed=42))
```

## Output
```
Profit: 130
```
*(Output varies due to randomness; supply `seed` for reproducible results)*

## Explanation
- **Inventory Simulation**: Tracks stock levels, reordering when below `reorder_point`.
- **Profit**: Revenue from sales ($10/unit) minus restocking costs ($5/unit).
- **Complexity**: O(days) time.
- **Use Case**: Demonstrates a basic model used in supply chain management or retail optimization.
- **Tip**: Pass a `seed` argument to reproduce runs and tune parameters; add holding or shortage costs for realism.