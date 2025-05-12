# Voting System

## Description
This snippet demonstrates a plurality voting system.

## Code
```python
from collections import Counter
votes = ["A", "B", "A", "C", "A"]  # Votes for candidates
count = Counter(votes)
winner = max(count, key=count.get)
print("Winner:", winner)
```

## Output
```
Winner: A
```

## Explanation
- **Voting System**: Implements plurality voting where the candidate with the most votes wins.
- **Logic**: Counts votes and selects the candidate with the highest count.
- **Complexity**: O(n) for n votes.
- **Use Case**: Used in elections or decision-making systems.
- **Best Practice**: Handle ties; validate votes; consider alternative voting methods.