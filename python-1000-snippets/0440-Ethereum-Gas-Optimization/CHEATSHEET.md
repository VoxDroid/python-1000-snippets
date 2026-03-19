# 0440-Ethereum-Gas-Optimization Cheatsheet

- Use `eth-tester` with `web3` for fast local testing without a real Ethereum node.
- Call `contract.constructor().estimate_gas(...)` to estimate deployment cost.
- Use `w3.eth.estimate_gas(tx)` to estimate gas for an arbitrary transaction.
- Solc optimizations can reduce deployment gas (compile with `optimize=True`).

Example:
```python
from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider

w3 = Web3(EthereumTesterProvider())
# ... deploy contract, estimate gas ...
```
