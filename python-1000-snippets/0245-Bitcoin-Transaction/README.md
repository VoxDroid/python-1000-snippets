# Bitcoin Transaction

## Description
This snippet demonstrates creating a Bitcoin transaction using `bitcoinlib`.

## Code
```python
# Note: Requires `bitcoinlib`. Install with `pip install bitcoinlib`
try:
    from bitcoinlib.wallets import Wallet
    wallet = Wallet.create("my_wallet")
    key = wallet.get_key()
    tx = wallet.send_to("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", 10000)
    print("Transaction ID:", tx.txid)
except ImportError:
    print("Mock Output: Transaction ID: <64-character hash>")
```

## Output
```
Mock Output: Transaction ID: <64-character hash>
```
*(Real output with `bitcoinlib`: `Transaction ID: <64-character hash>`)*

## Explanation
- **Bitcoin Transaction**: Creates a wallet and prepares a transaction using `bitcoinlib`.
- **Logic**: Generates a wallet and sends a small amount to an address.
- **Complexity**: O(1) for transaction creation (network for broadcasting).
- **Use Case**: Used for Bitcoin payments or wallet management.
- **Best Practice**: Use testnet for testing; secure keys; validate addresses.