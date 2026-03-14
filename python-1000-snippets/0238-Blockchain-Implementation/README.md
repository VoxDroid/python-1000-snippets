# Blockchain Implementation

## Description
This snippet demonstrates a simple blockchain with basic block hashing.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — basic blockchain with block hashing and chain display.
- `sample2.py` — validate the chain integrity after tampering.
- `sample3.py` — simple proof-of-work mining loop.

Run any of them with:

```bash
python python-1000-snippets/0238-Blockchain-Implementation/SAMPLES/sample1.py
```

## Output
Each script prints blockchain state and validation results.

## Explanation
- **Blockchain Implementation**: Creates a simple chain of blocks with SHA256 hashing.
- **Logic**: Each `Block` links to the previous block via `previous_hash`.
- **Complexity**: O(1) for hashing.
- **Use Case**: Used as a foundation for cryptocurrencies or tamper-proof ledgers.
- **Best Practice**: Add proof-of-work; validate chain integrity; secure data.