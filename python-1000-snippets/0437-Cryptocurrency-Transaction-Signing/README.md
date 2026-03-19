# Cryptocurrency Transaction Signing

## Description
This snippet demonstrates signing and verifying cryptocurrency transactions and messages using ECDSA (secp256k1).

## Requirements
- Python 3.8+
- `web3` (`pip install web3`)

## Samples
- `SAMPLES/sample1.py`: Sign a message and derive an Ethereum-style address from the public key.
- `SAMPLES/sample2.py`: Verify an ECDSA signature and detect tampering.
- `SAMPLES/sample3.py`: Recover an address from an ECDSA signature.

## Running
```bash
python python-1000-snippets/0437-Cryptocurrency-Transaction-Signing/SAMPLES/sample1.py
python python-1000-snippets/0437-Cryptocurrency-Transaction-Signing/SAMPLES/sample2.py
python python-1000-snippets/0437-Cryptocurrency-Transaction-Signing/SAMPLES/sample3.py
```

## Notes
- These examples use secp256k1 (the curve used by Bitcoin and Ethereum).
- In real systems, private keys must be stored securely (e.g., hardware wallets).
