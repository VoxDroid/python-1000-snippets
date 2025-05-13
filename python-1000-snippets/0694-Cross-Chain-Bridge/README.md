# Cross-Chain Bridge

## Description
This snippet demonstrates a cross-chain bridge for an e-commerce platform, transferring payment tokens between two blockchains for interoperability.

## Code
```python
# Cross-chain bridge for payment tokens
try:
    from typing import Dict
    from hashlib import sha256

    # Blockchain
    class Blockchain:
        def __init__(self, name: str):
            # Initialize blockchain with token balances
            self.name = name
            self.balances: Dict[str, int] = {}

        def lock_tokens(self, user_id: str, amount: int) -> str:
            # Lock tokens for transfer
            if self.balances.get(user_id, 0) >= amount:
                self.balances[user_id] -= amount
                return sha256(f"{user_id}{amount}".encode()).hexdigest()
            return "insufficient_funds"

        def mint_tokens(self, user_id: str, amount: int) -> None:
            # Mint tokens on target chain
            self.balances[user_id] = self.balances.get(user_id, 0) + amount

    # Simulate cross-chain transfer
    def transfer_tokens(user_id: str, amount: int) -> Dict[str, int]:
        # Transfer tokens between chains
        chain1 = Blockchain("Ethereum")
        chain2 = Blockchain("Binance")
        chain1.balances[user_id] = 1000
        lock_hash = chain1.lock_tokens(user_id, amount)
        if lock_hash != "insufficient_funds":
            chain2.mint_tokens(user_id, amount)
        return chain2.balances

    # Example usage
    result = transfer_tokens("U001", 100)
    print("Cross-chain bridge:", result)
except ImportError:
    print("Mock Output: Cross-chain bridge: {'U001': 100}")
```

## Output
```
Mock Output: Cross-chain bridge: {'U001': 100}
```
*(Real output: `Cross-chain bridge: {'U001': 100}`)*

## Explanation
- **Purpose**: Cross-chain bridges enable asset transfers between blockchains, enhancing interoperability.
- **Real-World Use Case**: In an e-commerce platform, a bridge transfers payment tokens between Ethereum and Binance chains, allowing flexible payment options.
- **Code Breakdown**:
  - The `Blockchain` class manages token balances with lock and mint operations.
  - The `transfer_tokens` function locks tokens on the source chain and mints them on the target chain.
  - The output shows the target chain’s balances.
- **Challenges**: Ensuring atomic transfers, preventing double-spending, and handling chain failures.
- **Integration**: Works with Sidechain Integration (Snippet 693) and Layer 2 Scaling (Snippet 695) for blockchain interoperability.
- **Complexity**: O(1) for transfer operations.
- **Best Practices**: Use secure oracles, validate transfers, monitor bridges, and test failure scenarios.