# 0243 - Web3 Integration Cheatsheet

## Quick Start
```bash
pip install web3 eth-tester
python python-1000-snippets/0243-Web3-Integration/SAMPLES/sample1.py
```

## Key Concepts
- `Web3(EthereumTesterProvider())` provides a local blockchain (no external node required).
- Accounts are pre-funded and available via `w3.eth.accounts`.
- Use `w3.eth.send_transaction(...)` for simple transfers.

## Common Patterns
- Get chain info:
  ```py
  print(w3.eth.chain_id, w3.eth.block_number)
  ```
- Send a transaction:
  ```py
  w3.eth.send_transaction({"from": a, "to": b, "value": w3.to_wei(1, "ether")})
  ```
- Deploy a contract:
  ```py
  tx = contract.constructor().transact({"from": acct})
  receipt = w3.eth.wait_for_transaction_receipt(tx)
  ```
