# 0240 - Smart Contract Cheatsheet

## Quick Start
```bash
pip install web3 eth-tester py-solc-x
python python-1000-snippets/0240-Smart-Contract/SAMPLES/sample1.py
```

## Key Concepts
- Compile Solidity using `py-solc-x` (`install_solc` + `compile_source`).
- Use `Web3(EthereumTesterProvider())` for a local in-memory chain.
- Deploy contracts with `contract.constructor().transact({"from": account})`.

## Common Tasks
- **Deploy & call**:
  ```py
  tx = contract.constructor().transact({"from": acct})
  receipt = w3.eth.wait_for_transaction_receipt(tx)
  deployed = w3.eth.contract(address=receipt.contractAddress, abi=abi)
  deployed.functions.get().call()
  ```

- **Handle events**:
  ```py
  events = deployed.events.ValueChanged().process_receipt(receipt)
  ```

- **Revert handling**:
  ```py
  try:
      deployed.functions.willRevert().transact({"from": acct})
  except Exception as e:
      print("reverted", e)
  ```
