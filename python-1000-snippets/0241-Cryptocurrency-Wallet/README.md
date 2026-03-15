# Cryptocurrency Wallet

## Description
This snippet demonstrates generating a Bitcoin testnet wallet, signing messages, and building a raw transaction using the `bit` library.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — generate a deterministic wallet and display address/public key details.
- `sample2.py` — sign and verify a message using a testnet private key.
- `sample3.py` — build and sign a raw Bitcoin transaction (offline; not broadcast).

Run any of them with:

```bash
python python-1000-snippets/0241-Cryptocurrency-Wallet/SAMPLES/sample1.py
```

## Output
Each sample prints key details and demonstrates real cryptographic signing or transaction encoding.

## Explanation
- **Cryptocurrency Wallet**: Uses `bit` to derive keys, addresses, and sign transactions.
- **Logic**: Creates a deterministic testnet private key, derives the public address, signs messages, and constructs a signed raw transaction.
- **Use Case**: Useful for Bitcoin wallet tooling, offline transaction creation, and signing.
- **Best Practice**: Keep private keys secure; avoid reusing keys; only broadcast transactions on a real network after validating inputs.
