# 0439-Web3-Smart-Contract-Interaction Cheatsheet

- Use `Web3(EthereumTesterProvider())` for local in-memory blockchain testing.
- Deploy a contract with `contract.constructor().transact(...)` and use the returned address.
- Use `contract.functions.<name>().transact(...)` for state-changing calls and `.call()` for view calls.
- Use `Account.sign_transaction()` and `web3.eth.send_raw_transaction()` to send signed raw transactions.
- Use `contract.events.<EventName>().createFilter()` to read events.

## Notes
- Tests should use deterministic accounts / keys when possible.
- In production, use a real Ethereum provider and manage private keys securely.
