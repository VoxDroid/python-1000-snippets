# Bitcoin Transaction

## Description
This snippet demonstrates creating and signing Bitcoin transactions locally using the `bit` library.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — generate a deterministic testnet keypair and display address information.
- `sample2.py` — sign a message using a Bitcoin key and verify it.
- `sample3.py` — build and sign a raw Bitcoin transaction using a constructed UTXO.

Run any of them with:

```bash
python python-1000-snippets/0245-Bitcoin-Transaction/SAMPLES/sample1.py
```

## Output
Each sample prints outputs related to addresses, signatures, and a raw signed transaction.

## Explanation
- **Bitcoin Transaction**: Builds and signs transactions offline without broadcasting.
- **Logic**: Uses `bit` to generate keys, sign messages, and construct raw transactions from UTXOs.
- **Use Case**: Useful for offline signing workflows, hardware wallets, and testing transaction encoding.
- **Best Practice**: Keep private keys secure; verify UTXO data before signing; never reuse addresses.
