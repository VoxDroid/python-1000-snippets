# Proof of Work

## Description
This snippet demonstrates a proof-of-work (PoW) mechanism for an e-commerce blockchain, securing order transactions by solving a computational puzzle.

## Code
```python
# Proof of work for blockchain
try:
    from hashlib import sha256

    # Block with PoW
    class Block:
        def __init__(self, transactions: list[str], previous_hash: str):
            # Initialize block with transactions
            self.transactions = transactions
            self.previous_hash = previous_hash
            self.nonce = 0
            self.hash = self.mine()

        def compute_hash(self) -> str:
            # Compute hash with nonce
            return sha256((str(self.transactions) + self.previous_hash + str(self.nonce)).encode()).hexdigest()

        def mine(self, difficulty: int = 2) -> str:
            # Mine block until hash starts with difficulty zeros
            target = "0" * difficulty
            while True:
                hash_result = self.compute_hash()
                if hash_result.startswith(target):
                    return hash_result
                self.nonce += 1

    # Simulate PoW
    def secure_order(order_id: str) -> str:
        # Create and mine block
        block = Block([f"Order {order_id} confirmed"], "0")
        return block.hash

    # Example usage
    result = secure_order("O001")
    print("Proof of work:", result)
except ImportError:
    print("Mock Output: Proof of work: <hash>")
```

## Output
```
Mock Output: Proof of work: <hash>
```
*(Real output: `Proof of work: <sha256_hash_with_leading_zeros>`)*

## Explanation
- **Purpose**: Proof of work secures a blockchain by requiring computational effort to add blocks, preventing tampering.
- **Real-World Use Case**: In an e-commerce blockchain, PoW ensures order transactions are securely recorded, deterring fraudulent modifications.
- **Code Breakdown**:
  - The `Block` class includes a nonce for PoW.
  - The `mine` method finds a hash with leading zeros by incrementing the nonce.
  - The `secure_order` function mines a block for an order.
- **Challenges**: High energy consumption, scaling for high transaction rates, and balancing difficulty.
- **Integration**: Works with Blockchain Consensus (Snippet 687) and Proof of Stake (Snippet 689) for security.
- **Complexity**: O(2^d) for difficulty d; depends on hash target.
- **Best Practices**: Adjust difficulty dynamically, use efficient hashing, monitor mining, and consider alternatives.