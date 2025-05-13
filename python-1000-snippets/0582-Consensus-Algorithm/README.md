# Consensus Algorithm

## Description
This snippet demonstrates a simplified majority vote consensus.

## Code
```python
try:
    def consensus(votes):
        return sum(votes) > len(votes) / 2
    votes = [1, 1, 0]
    print("Consensus reached:", consensus(votes))
except ImportError:
    print("Mock Output: Consensus reached: True")
```

## Output
```
Mock Output: Consensus reached: True
```
*(Real output: `Consensus reached: True`)*

## Explanation
- **Consensus Algorithm**: Achieves agreement among nodes.
- **Logic**: Returns True if majority votes are 1.
- **Complexity**: O(n) for n votes.
- **Use Case**: Used in distributed systems like Raft.
- **Best Practice**: Handle partitions; ensure fault tolerance; log votes.