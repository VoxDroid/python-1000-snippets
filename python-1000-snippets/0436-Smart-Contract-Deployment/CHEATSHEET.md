# 0436-Smart-Contract-Deployment Cheatsheet

- Use `solcx` to compile Solidity sources from Python.
- Deploy contracts using `Web3.eth.contract(abi=..., bytecode=...)`.
- Use `contract.constructor().transact()` to deploy, and `contract.functions.<name>().call()`/`transact()` to interact.

## Compile Solidity
```py
import solcx
solcx.install_solc('0.8.0')
compiled = solcx.compile_source(source, output_values=['abi','bin'])
```

## Deploy contract
```py
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = SimpleStorage.constructor().transact({'from': acct})
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract = w3.eth.contract(address=receipt.contractAddress, abi=abi)
```

## Notes
- `eth-tester` provides an in-memory EVM for testing without network dependencies.
- For mainnet, connect to a provider like Infura or Alchemy.
