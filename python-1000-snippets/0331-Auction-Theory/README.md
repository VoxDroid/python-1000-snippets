# Auction Theory

## Description
This snippet demonstrates a first-price sealed-bid auction simulation.

## Code
```python
import numpy as np
np.random.seed(42)
bids = np.random.randint(10, 100, 5)  # 5 bidders
winner = np.argmax(bids)
price = bids[winner]
print("Winner Index:", winner, "Price:", price)
```

## Output
```
Winner Index: 2 Price: 81
```

## Explanation
- **Auction Theory**: Simulates a first-price sealed-bid auction where the highest bidder wins and pays their bid.
- **Logic**: Generates random bids, selects the highest, and determines the price.
- **Complexity**: O(n) for n bidders.
- **Use Case**: Used in economics to model bidding strategies.
- **Best Practice**: Model bidder strategies; handle ties; validate bid ranges.