# Cryptocurrency Transaction Signing

## Description
This snippet demonstrates signing a transaction using `ecdsa`.

## Code
```python
# Note: Requires `ecdsa`. Install with `pip install ecdsa`
try:
    from ecdsa import SigningKey, SECP256k1
    sk = SigningKey.generate(curve=SECP256k1)
    message = b"Transaction"
    signature = sk.sign(message)
    print("Signature:", signature.hex()[:10])
except ImportError:
    print("Mock Output: Signature: bb5f24bf75")
```

## Output
```
Mock Output: Signature: bb5f24bf75
```
*(Real output with `ecdsa`: `Signature: <hex prefix>`)*

## Explanation
- **Cryptocurrency Transaction Signing**: Signs a transaction with ECDSA.
- **Logic**: Generates a key and signs a message.
- **Complexity**: O(1) for signing.
- **Use Case**: Used in cryptocurrency wallets for transaction authorization.
- **Best Practice**: Secure private keys; use standard curves; verify signatures.