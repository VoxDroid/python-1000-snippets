# 0244 - Ethereum Transaction Cheatsheet

## Quick Start
```bash
pip install web3 eth-tester
python python-1000-snippets/0244-Ethereum-Transaction/SAMPLES/sample1.py
```

## Key Concepts
- Use `Web3(EthereumTesterProvider())` for a fully local Ethereum chain.
- Transactions require `from`, `to`, `value`, and optionally `gas`/`gasPrice`.
- Use `acct.sign_transaction(tx)` + `send_raw_transaction(raw)` for offline signing.

## Common Patterns
- Check balances & nonces:
  ```py
  w3.eth.get_balance(addr)
  w3.eth.get_transaction_count(addr)
  ```
- Send a transaction:
  ```py
  tx_hash = w3.eth.send_transaction(tx)
  receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
  ```
- Sign and broadcast raw tx:
  ```py
  signed = acct.sign_transaction(tx)
  w3.eth.send_raw_transaction(signed.raw_transaction)
  ```
