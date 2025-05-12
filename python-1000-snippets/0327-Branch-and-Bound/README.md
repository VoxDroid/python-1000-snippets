# Branch and Bound

## Description
This snippet demonstrates branch and bound for a knapsack problem.

## Code
```python
def knapsack(values, weights, capacity):
    n = len(values)
    best_value = 0
    def bound(items, weight, value):
        if weight > capacity:
            return 0
        return value + sum(values[i] for i in range(items, n) if weight + sum(weights[items:i]) <= capacity)
    
    def branch(items, weight, value):
        nonlocal best_value
        if weight <= capacity and value > best_value:
            best_value = value
        if items == n or bound(items, weight, value) <= best_value:
            return
        branch(items + 1, weight + weights[items], value + values[items])
        branch(items + 1, weight, value)
    
    branch(0, 0, 0)
    return best_value

print("Max Value:", knapsack([60, 100], [10, 20], 20))
```

## Output
```
Max Value: 100
```

## Explanation
- **Branch and Bound**: Solves knapsack by exploring branches with bounds.
- **Logic**: Prunes branches based on estimated maximum value.
- **Complexity**: O(2^n) worst case, improved by pruning.
- **Use Case**: Used for combinatorial optimization like TSP.
- **Best Practice**: Tighten bounds; optimize branching; validate inputs.