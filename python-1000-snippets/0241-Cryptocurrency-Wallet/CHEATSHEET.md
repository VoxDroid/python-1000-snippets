# 0241 - Cryptocurrency Wallet Cheatsheet

## Quick Start
```bash
pip install bit
python python-1000-snippets/0241-Cryptocurrency-Wallet/SAMPLES/sample1.py
```

## Common Tasks
- Generate a new keypair (testnet):
  ```python
  from bit import PrivateKeyTestnet
  key = PrivateKeyTestnet()
  print(key.address)
  ```

- Sign and verify a message:
  ```python
  signature = key.sign(b"hello")
  assert key.verify(b"hello", signature)
  ```

- Create a raw transaction (offline):
  ```python
  from bit.network.meta import Unspent
  # ... build unspents and call key.create_transaction(...)
  ```

## Notes
- `PrivateKeyTestnet` creates testnet addresses (start with `m` or `n`).
- Keep private keys secret; do not commit them to source control.
