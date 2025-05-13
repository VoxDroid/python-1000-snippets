# A/B Testing Framework

## Description
This snippet demonstrates A/B testing with random assignment.

## Code
```python
try:
    import random
    def assign_variant():
        return "A" if random.random() < 0.5 else "B"
    print("Assigned variant:", assign_variant())
except ImportError:
    print("Mock Output: Assigned variant: A")
```

## Output
```
Mock Output: Assigned variant: A
```
*(Real output: `Assigned variant: A` or `B`)*

## Explanation
- **A/B Testing Framework**: Assigns users to test variants.
- **Logic**: Randomly assigns variant A or B.
- **Complexity**: O(1) per assignment.
- **Use Case**: Used for comparing feature performance.
- **Best Practice**: Track metrics; ensure fair splits; analyze results.