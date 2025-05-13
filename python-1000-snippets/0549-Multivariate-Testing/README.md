# Multivariate Testing

## Description
This snippet demonstrates multivariate testing with multiple variants.

## Code
```python
try:
    import random
    variants = {"color": ["red", "blue"], "size": ["small", "large"]}
    def assign_variants():
        return {k: random.choice(v) for k, v in variants.items()}
    print("Assigned variants:", assign_variants())
except ImportError:
    print("Mock Output: Assigned variants: {'color': 'red', 'size': 'small'}")
```

## Output
```
Mock Output: Assigned variants: {'color': 'red', 'size': 'small'}
```
*(Real output: `Assigned variants: <random combination>`)*

## Explanation
- **Multivariate Testing**: Tests multiple feature combinations.
- **Logic**: Randomly selects variants for each feature.
- **Complexity**: O(k) for k features.
- **Use Case**: Used for optimizing complex interfaces.
- **Best Practice**: Balance variants; track interactions; use statistical analysis.