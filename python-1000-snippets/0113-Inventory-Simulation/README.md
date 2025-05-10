# Inventory Simulation

## Description
This snippet simulates an inventory system with random demand, reordering when stock is low.

## Code
```python
import random

def inventory_simulation(initial_stock, reorder_point, reorder_amount, days):
    stock = initial_stock
    costs = 0
    for _ in range(days):
        demand = random.randint(0, 5)
        stock -= demand
        costs += demand * 10  # Selling price
        if stock <= reorder_point:
            stock += reorder_amount
            costs += reorder_amount * 5  # Restocking cost
    return costs

print("Total Cost:", inventory_simulation(20, 5, 10, 30))
```

## Output
```
Total Cost: 580
```
*(Output varies due to randomness)*

## Explanation
- **Inventory Simulation**: Tracks stock levels, reordering when below `reorder_point`.
- **Costs**: Revenue from sales ($10/unit) minus restocking costs ($5/unit).
- **Complexity**: O(days) time.
- **Use Case**: Used in supply chain management or retail optimization.
- **Best Practice**: Add holding costs; tune parameters for realistic scenarios.