# 0435-Merkle-Tree-Verification Cheatsheet

- A Merkle tree hashes pairs of nodes up to a single root hash.
- Proof of inclusion is a list of sibling hashes to recompute the root.

## Compute Merkle root
```py
import hashlib

def merkle_root(leaves):
    nodes = [hashlib.sha256(l).digest() for l in leaves]
    while len(nodes) > 1:
        if len(nodes) % 2 == 1:
            nodes.append(nodes[-1])
        nodes = [hashlib.sha256(nodes[i] + nodes[i+1]).digest() for i in range(0, len(nodes), 2)]
    return nodes[0]
```

## Notes
- Keep leaf order consistent (e.g., sorted by some deterministic key) to avoid mismatched roots.
- Reuse proofs to verify inclusion without sharing all leaves.
