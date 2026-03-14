# 0239-Merkle-Tree Cheatsheet

## Run
```bash
python python-1000-snippets/0239-Merkle-Tree/SAMPLES/sample1.py
python python-1000-snippets/0239-Merkle-Tree/SAMPLES/sample2.py
python python-1000-snippets/0239-Merkle-Tree/SAMPLES/sample3.py
```

## Notes
* Merkle trees allow verification of data inclusion with O(log n) proof size.
* For odd numbers of leaves, duplicate the last leaf when building parents.
* A Merkle proof is a list of sibling hashes needed to recompute the root.
