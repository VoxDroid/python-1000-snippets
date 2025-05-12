# Game Theory

## Description
This snippet demonstrates a simple game theory payoff matrix analysis.

## Code
```python
import numpy as np
payoff = np.array([[[3, 3], [0, 5]], [[5, 0], [1, 1]]])  # Prisoner's Dilemma
strategy1 = np.argmax(payoff[0, :, 0])  # Player 1's best response
strategy2 = np.argmax(payoff[:, 0, 1])  # Player 2's best response
print("Strategies:", strategy1, strategy2)
```

## Output
```
Strategies: 0 0
```

## Explanation
- **Game Theory**: Analyzes a payoff matrix to find each player's best response to the opponent’s fixed strategy.
- **Logic**: Computes each player’s best response assuming the opponent’s strategy is fixed (not computing Nash equilibrium here).
- **Complexity**: O(n) for n strategies (simplified analysis).
- **Use Case**: Modeling competitive scenarios like economics, auctions, or decision-making.
- **Best Practice**: Handle mixed strategies (where players may randomize choices); validate payoffs; check for equilibrium or stable outcomes.
