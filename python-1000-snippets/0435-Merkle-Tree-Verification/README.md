# Merkle Tree Verification

## Description
This snippet demonstrates a simplified Merkle tree for data verification.

## Code
```python
try:
    import hashlib
    def merkle_root(leaves):
        if not leaves:
            return ""
        while len(leaves) > 1:
            temp = []
            for i in range(0, len(leaves), 2):
                pair = leaves[i:i+2]
                combined = pair[0] + (pair[1] if len(pair) > 1 else pair[0])
                temp.append(hashlib.sha256(combined.encode()).hexdigest())
            leaves = temp
        return leaves[0]
    
    leaves = ["data1", "data2"]
    print("Merkle Root:", merkle_root(leaves)[:10])
except ImportError:
    print("Mock Output: Merkle Root: 53ddc03623")
```

## Output
```
Mock Output: Merkle Root: 53ddc03623
```
*(Real output: `Merkle Root: <hash prefix>`)*

## Explanation
- **Merkle Tree Verification**: Computes a Merkle root for data integrity.
- **Logic**: Hashes pairs of leaves iteratively to form a root.
- **Complexity**: O(n log n) for n leaves.
- **Use Case**: Used in blockchains for efficient data verification.
- **Best Practice**: Use secure hashing; handle odd leaf counts; test tree structure.