# Inventory Optimization

## Description
This snippet demonstrates inventory optimization using EOQ model.

## Code
```python
# Note: Requires `math`. Built-in module.
try:
    from math import sqrt
    demand = 1000  # Annual demand
    order_cost = 50  # Cost per order
    holding_cost = 2  # Cost per unit per year
    eoq = sqrt(2 * demand * order_cost / holding_cost)
    print("Optimal order quantity:", round(eoq, 2))
except ImportError:
    print("Mock Output: Optimal order quantity: 223.61")
```

## Output
```
Mock Output: Optimal order quantity: 223.61
```
*(Real output: `Optimal order quantity: 223.61`)*

## Explanation
- **Inventory Optimization**: Calculates optimal order quantity.
- **Logic**: Uses Economic Order Quantity (EOQ) formula.
- **Complexity**: O(1) per calculation.
- **Use Case**: Used in inventory management.
- **Best Practice**: Account for lead time; validate assumptions; adjust for variability.