# 0437-Cryptocurrency-Transaction-Signing Cheatsheet

- Cryptocurrency signatures use ECDSA over secp256k1.
- An address is derived from the public key (e.g., Ethereum uses keccak-256 of the uncompressed key).

## Sign a message
```py
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
signature = key.sign(message, ec.ECDSA(hashes.SHA256()))
```

## Verify a signature
```py
public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
```

## Recover Ethereum address from public key
```py
from eth_utils import keccak
addr = keccak(uncompressed_pubkey)[-20:]
```
