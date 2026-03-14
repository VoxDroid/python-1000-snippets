# Merkle Tree

## Description
This snippet demonstrates a Merkle Tree for efficient data verification.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — build a Merkle tree and print the root hash.
- `sample2.py` — create a Merkle proof for a leaf and print it.
- `sample3.py` — verify a Merkle proof against a root hash.

Run any of them with:

```bash
python python-1000-snippets/0239-Merkle-Tree/SAMPLES/sample1.py
```

## Output
Each script prints the computed Merkle root and/or proof verification results.

## Explanation
- **Merkle Tree**: Builds a binary tree of hashed data for efficient integrity checks.
- **Logic**: Hash leaves, combine pairs to build upper layers, and compute a root; proofs show inclusion with minimal data.
- **Complexity**: O(n) to build the tree, O(log n) to verify a proof.
- **Use Case**: Used in blockchains for compact transaction verification.
- **Best Practice**: Handle odd leaf counts (duplicate last leaf), use secure hashing, and verify Merkle proofs before trusting data.