# Ethereum Transaction

## Description
This snippet demonstrates sending an Ethereum transaction using `web3.py`.

## Code
```python
# Note: Requires `web3`. Install with `pip install web3`
try:
    from web3 import Web3
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    account = w3.eth.account.create()
    tx = {
        "to": "0x1234567890123456789012345678901234567890",
        "value": w3.to_wei(1, "ether"),
        "gas": 21000,
        "gasPrice": w3.to_wei(20, "gwei"),
        "nonce": 0
    }
    print("Transaction prepared for:", account.address)
except ImportError:
    print("Mock Output: Transaction prepared for: 0x...")
```

## Output
```
Mock Output: Transaction prepared for: 0x...
```
*(Real output with `web3`: `Transaction prepared for: 0x...`)*

## Explanation
- **Ethereum Transaction**: Prepares a transaction using `web3.py`.
- **Logic**: Creates an account and builds a transaction dictionary.
- **Complexity**: O(1) for preparation (network latency for sending).
- **Use Case**: Used for sending Ether or interacting with smart contracts.
- **Best Practice**: Sign transactions; validate addresses; use real node for sending.