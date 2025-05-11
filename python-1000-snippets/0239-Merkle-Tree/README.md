# Merkle Tree

## Description
This snippet demonstrates a Merkle Tree for efficient data verification.

## Code
```python
import hashlib

class MerkleTree:
    def __init__(self, data):
        self.leaves = [hashlib.sha256(d.encode()).hexdigest() for d in data]
        self.root = self.build_tree(self.leaves)
    def build_tree(self, leaves):
        if len(leaves) == 1:
            return leaves[0]
        parents = []
        for i in range(0, len(leaves), 2):
            combined = leaves[i] + (leaves[i+1] if i+1 < len(leaves) else leaves[i])
            parents.append(hashlib.sha256(combined.encode()).hexdigest())
        return self.build_tree(parents)

tree = MerkleTree(["tx1", "tx2", "tx3", "tx4"])
print("Merkle Root:", tree.root)
```

## Output
```
Merkle Root: <64-character SHA256 hash>
```

## Explanation
- **Merkle Tree**: Builds a binary tree of hashed transactions for efficient verification.
- **Logic**: Hashes leaves and recursively combines pairs to form the root.
- **Complexity**: O(n log n) for n transactions.
- **Use Case**: Used in blockchains for compact transaction verification.
- **Best Practice**: Handle odd leaf counts; use secure hashing; verify proofs.