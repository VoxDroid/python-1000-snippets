# 0245 - Bitcoin Transaction Cheatsheet

## Quick Start
```bash
pip install bit
python python-1000-snippets/0245-Bitcoin-Transaction/SAMPLES/sample1.py
```

## Key Concepts
- `PrivateKeyTestnet` creates testnet keys and addresses.
- `key.sign(message)` produces a DER signature; verify with `key.verify(signature, message)`.
- `key.create_transaction(outputs, unspents=[...])` builds a signed raw tx from UTXOs.

## Common Patterns
- Generate a key:
  ```py
  key = PrivateKeyTestnet()
  print(key.address)
  ```
- Create a fake UTXO for offline signing:
  ```py
  from bit.network.meta import Unspent
  utxo = Unspent(amount=..., script=key.scriptcode, txid='00'*32, txindex=0)
  ```
- Derive txid:
  ```py
  import hashlib
  raw_bytes = bytes.fromhex(raw)
  txid = hashlib.sha256(hashlib.sha256(raw_bytes).digest()).digest()[::-1].hex()
  ```
