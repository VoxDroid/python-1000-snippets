# Web3 Integration

## Description
This snippet demonstrates connecting to Ethereum using `web3.py`.

## Code
```python
# Note: Requires `web3`. Install with `pip install web3`
try:
    from web3 import Web3
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    print("Connected:", w3.is_connected())
except ImportError:
    print("Mock Output: Connected: True")
```

## Output
```
Mock Output: Connected: True
```
*(Real output with `web3`: `Connected: True` if node is running)*

## Explanation
- **Web3 Integration**: Connects to an Ethereum node using `web3.py`.
- **Logic**: Initializes a Web3 instance and checks connection status.
- **Complexity**: O(1) for connection check (network latency varies).
- **Use Case**: Used for interacting with Ethereum blockchain or smart contracts.
- **Best Practice**: Use secure providers; handle node failures; ensure node is running.