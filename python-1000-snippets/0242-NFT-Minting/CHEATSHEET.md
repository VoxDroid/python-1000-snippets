# 0242 - NFT Minting Cheatsheet

## Quick Start
```bash
pip install web3 eth-tester py-solc-x
python python-1000-snippets/0242-NFT-Minting/SAMPLES/sample1.py
```

## Key Concepts
- Compile Solidity with `py-solc-x`.
- Use `Web3(EthereumTesterProvider())` for an in-memory local Ethereum chain.
- Deploy a contract and call its functions using `contract.functions.<name>().transact(...)`.

## Common Patterns
- Deploy contract:
  ```py
  tx_hash = contract.constructor(...).transact({"from": acct})
  receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
  deployed = w3.eth.contract(address=receipt.contractAddress, abi=abi)
  ```

- Call view functions:
  ```py
  deployed.functions.ownerOf(1).call()
  ```

- Send transactions:
  ```py
  deployed.functions.mint(...).transact({"from": acct})
  ```
