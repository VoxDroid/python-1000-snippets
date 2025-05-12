# Greedy Algorithm

## Description
This snippet demonstrates a greedy algorithm for coin change.

## Code
```python
def coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin
    return result

print("Coins for 67:", coin_change([25, 10, 5, 1], 67))
```

## Output
```
Coins for 67: [25, 25, 10, 5, 1, 1]
```

## Explanation
- **Greedy Algorithm**: Selects coins to minimize count for a given amount.
- **Logic**: Chooses largest possible coins iteratively.
- **Complexity**: O(n + a) for n coins, a amount.
- **Use Case**: Used for problems like scheduling or Huffman coding.
- **Best Practice**: Verify optimality; handle edge cases; validate inputs.