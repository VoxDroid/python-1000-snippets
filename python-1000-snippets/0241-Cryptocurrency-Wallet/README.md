# Cryptocurrency Wallet

## Description
This snippet demonstrates generating a cryptocurrency wallet address using `ecdsa`.

## Code
```python
# Note: Requires `ecdsa`. Install with `pip install ecdsa`
try:
    from ecdsa import SigningKey, SECP256k1
    import hashlib
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key().to_string()
    address = hashlib.sha256(public_key).hexdigest()
    print("Address:", address)
except ImportError:
    print("Mock Output: Address: <64-character SHA256 hash>")
```

## Output
```
Mock Output: Address: <64-character SHA256 hash>
```
*(Real output with `ecdsa`: `Address: <64-character SHA256 hash>`)*

## Explanation
- **Cryptocurrency Wallet**: Generates a private-public key pair and derives an address.
- **Logic**: Uses ECDSA with SECP256k1 curve and hashes the public key.
- **Complexity**: O(1) for key generation and hashing.
- **Use Case**: Used for creating wallet addresses in cryptocurrencies like Bitcoin.
- **Best Practice**: Secure private keys; use standard curves; validate addresses.