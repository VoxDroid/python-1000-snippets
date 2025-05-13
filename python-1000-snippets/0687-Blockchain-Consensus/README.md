# Blockchain Consensus

## Description
This snippet demonstrates a simplified blockchain consensus for an e-commerce platform, recording order transactions in a chain with majority agreement.

## Code
```python
# Blockchain consensus for order transactions
try:
    from typing import List
    from hashlib import sha256

    # Block for transactions
    class Block:
        def __init__(self, transactions: List[str], previous_hash: str):
            # Initialize block with transactions and hash
            self.transactions = transactions
            self.previous_hash = previous_hash
            self.hash = self.compute_hash()

        def compute_hash(self) -> str:
            # Compute block hash
            return sha256((str(self.transactions) + self.previous_hash).encode()).hexdigest()

    # Blockchain node
    class BlockchainNode:
        def __init__(self):
            # Initialize chain with genesis block
            self.chain: List[Block] = [Block(["genesis"], "0")]

        def add_block(self, transactions: List[str]) -> bool:
            # Add block with consensus (simulated majority)
            new_block = Block(transactions, self.chain[-1].hash)
            self.chain.append(new_block)
            return True  # Simulate majority agreement

    # Simulate blockchain
    def record_order(order_id: str) -> str:
        # Create node and add transaction
        node = BlockchainNode()
        node.add_block([f"Order {order_id} confirmed"])
        return node.chain[-1].hash

    # Example usage
    result = record_order("O001")
    print("Blockchain consensus:", result)
except ImportError:
    print("Mock Output: Blockchain consensus: <hash>")
```

## Output
```
Mock Output: Blockchain consensus: <hash>
```
*(Real output: `Blockchain consensus: <sha256_hash>`)*

## Explanation
- **Purpose**: Blockchain consensus ensures a tamper-proof, agreed-upon transaction ledger across nodes.
- **Real-World Use Case**: In an e-commerce platform, a blockchain records order transactions, ensuring transparency and auditability for supply chain tracking.
- **Code Breakdown**:
  - The `Block` class represents a block with transactions and a hash.
  - The `BlockchainNode` class maintains a chain and adds blocks with simulated consensus.
  - The `record_order` function records an order transaction.
- **Challenges**: Achieving consensus, managing chain size, and handling forks.
- **Integration**: Works with Proof of Work (Snippet 688) and Proof of Stake (Snippet 689) for consensus mechanisms.
- **Complexity**: O(1) for block addition; scales with chain length.
- **Best Practices**: Use established blockchains, validate transactions, monitor forks, and ensure security.