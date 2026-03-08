# 0113-Inventory-Simulation Cheatsheet

- **Purpose**: simulate stock levels with random daily demand and automatic reordering.
- **Key parameters**:
  - `initial_stock`: starting units on hand
  - `reorder_point`: level triggering a new order
  - `reorder_amount`: units added on reorder
  - `days`: total simulation days
  - `demand_max`: upper bound for uniform random demand each day
  - `seed`: optional `int` for reproducible randomness
- **Return value**: total profit (sales revenue minus restocking cost).

```python
from inventory_simulation import inventory_simulation

# deterministic run
profit = inventory_simulation(20, 5, 10, 30, seed=1)
print(profit)  # reproducible result

# compare reorder strategies
for rp in (3, 5, 7):
    print(rp, inventory_simulation(20, rp, 10, 100, seed=42))
```

- Use loops or Monte Carlo trials to analyze cost distributions.
- Seed the RNG if you need repeatable behavior during testing.
