# Smart Contract

## Description
This snippet demonstrates deploying and interacting with a smart contract on a local Ethereum test chain using `web3`, `eth-tester`, and `py-solc-x`.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — deploy a simple storage contract, set and get a value.
- `sample2.py` — emit and read events from a contract.
- `sample3.py` — call a contract method that reverts and handle the exception.

Run any of them with:

```bash
python python-1000-snippets/0240-Smart-Contract/SAMPLES/sample1.py
```

## Output
Each sample prints contract interaction results and demonstrates real execution on an in-memory Ethereum chain.

## Explanation
- **Smart Contract**: Uses Solidity compiled by `py-solc-x`, deployed on an in-memory blockchain using `eth-tester`.
- **Logic**: Deploy contract, call functions, query state, handle events, and handle transaction reverts.
- **Use Case**: Useful for local smart contract development and testing without requiring an external node.
- **Best Practice**: Validate transaction receipts, handle revert reasons, and use proper gas estimation.
