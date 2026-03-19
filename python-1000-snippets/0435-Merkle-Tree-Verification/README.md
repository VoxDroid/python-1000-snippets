# Merkle Tree Verification

## Description
This snippet demonstrates computing a Merkle tree root and verifying inclusion proofs.

## Requirements
- Python 3.8+

## Samples
- `SAMPLES/sample1.py`: Compute the Merkle root for a list of leaves.
- `SAMPLES/sample2.py`: Generate and verify a Merkle inclusion proof for a leaf.
- `SAMPLES/sample3.py`: Show that changing the leaf or root invalidates the proof.

## Running
```bash
python python-1000-snippets/0435-Merkle-Tree-Verification/SAMPLES/sample1.py
python python-1000-snippets/0435-Merkle-Tree-Verification/SAMPLES/sample2.py
python python-1000-snippets/0435-Merkle-Tree-Verification/SAMPLES/sample3.py
```

## Notes
- Merkle trees provide efficient proof of inclusion without sending all leaves.
- Commonly used in blockchains and data integrity systems.
