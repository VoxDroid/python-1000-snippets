# Blockchain Implementation

## Description
This snippet demonstrates a simple blockchain with basic block hashing.

## Code
```python
import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    def calculate_hash(self):
        return hashlib.sha256(f"{self.index}{self.data}{self.timestamp}{self.previous_hash}".encode()).hexdigest()

blockchain = [Block(0, "Genesis", "0")]
blockchain.append(Block(1, "Transaction1", blockchain[0].hash))
print("Block Hash:", blockchain[1].hash)
```

## Output
```
Block Hash: <64-character SHA256 hash>
```

## Explanation
- **Blockchain Implementation**: Creates a simple chain of blocks with SHA256 hashing.
- **Logic**: Each `Block` links to the previous block via `previous_hash`.
- **Complexity**: O(1) for hashing.
- **Use Case**: Used as a foundation for cryptocurrencies or tamper-proof ledgers.
- **Best Practice**: Add proof-of-work; validate chain integrity; secure data.