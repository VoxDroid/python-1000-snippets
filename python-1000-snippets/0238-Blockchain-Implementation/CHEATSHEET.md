# 0238-Blockchain-Implementation Cheatsheet

## Run
```bash
python python-1000-snippets/0238-Blockchain-Implementation/SAMPLES/sample1.py
python python-1000-snippets/0238-Blockchain-Implementation/SAMPLES/sample2.py
python python-1000-snippets/0238-Blockchain-Implementation/SAMPLES/sample3.py
```

## Notes
* Each block includes an index, timestamp, data, previous hash, and its own hash.
* Chain validation ensures `previous_hash` matches and recomputed hashes match stored hashes.
* Proof-of-work adds difficulty by requiring hashes with leading zeros (can be slow).
