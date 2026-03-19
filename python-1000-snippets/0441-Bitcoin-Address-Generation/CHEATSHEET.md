# 0441-Bitcoin-Address-Generation Cheatsheet

- Use `cryptography` to generate secp256k1 keys.
- Bitcoin P2PKH addresses are derived via: `RIPEMD160(SHA256(pubkey))` + version byte + checksum, then base58-check encoded.
- WIF encodes a private key with a network prefix, optional compressed flag, and checksum.

Quick start:
```python
# Generate a new address
priv, addr = generate_keypair()
print(addr)
```

Validate by deriving the address from the WIF:
```python
priv_bytes = wif_to_private_key(wif)
# derive pubkey/address from priv_bytes
```
