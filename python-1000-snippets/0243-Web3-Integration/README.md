# Web3 Integration

## Description
This snippet demonstrates connecting to Ethereum using `web3.py` and the in-memory `eth-tester` provider for local testing.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — connect to an in-memory Ethereum chain and print the latest block number.
- `sample2.py` — check account balances and send a transaction between pre-funded accounts.
- `sample3.py` — deploy a simple contract and call a function.

Run any of them with:

```bash
python python-1000-snippets/0243-Web3-Integration/SAMPLES/sample1.py
```

## Output
Each sample prints connection status and demonstrates basic Web3 interactions against a local in-memory Ethereum chain.

## Explanation
- **Web3 Integration**: Uses `web3.py` to interact with an Ethereum provider.
- **Logic**: Uses `eth-tester` for a local blockchain without needing an external node.
- **Use Case**: Useful for quick smart contract testing and local development.
- **Best Practice**: Use a real provider (Infura, Alchemy, local node) for production and handle RPC errors.
