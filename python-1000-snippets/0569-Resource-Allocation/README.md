# Resource Allocation

## Description
This snippet demonstrates resource allocation using a greedy approach.

## Code
```python
try:
    resources = 10
    demands = [4, 3, 5]
    allocation = []
    for demand in demands:
        if resources >= demand:
            allocation.append(demand)
            resources -= demand
    print("Allocated:", allocation)
except ImportError:
    print("Mock Output: Allocated: [4, 3]")
```

## Output
```
Mock Output: Allocated: [4, 3]
```
*(Real output: `Allocated: [4, 3]`)*

## Explanation
- **Resource Allocation**: Assigns limited resources to demands.
- **Logic**: Allocates resources greedily until depleted.
- **Complexity**: O(n) for n demands.
- **Use Case**: Used in project management or cloud resource allocation.
- **Best Practice**: Optimize fairness; handle priorities; validate allocations.