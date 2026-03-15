# Ethereum Transaction

## Description
This snippet demonstrates building and sending Ethereum transactions using `web3.py` with a local in-memory chain (`eth-tester`).

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — examine account balances and nonces on the local chain.
- `sample2.py` — send Ether between pre-funded eth-tester accounts.
- `sample3.py` — sign a raw transaction with a local private key and broadcast it.

Run any of them with:

```bash
python python-1000-snippets/0244-Ethereum-Transaction/SAMPLES/sample1.py
```

## Output
Each sample prints transaction details and demonstrates real transaction construction/execution on an in-memory Ethereum chain.

## Explanation
- **Ethereum Transaction**: Uses `web3.py` to build, sign, and broadcast transactions.
- **Logic**: Interacts with an eth-tester provider to keep everything local and deterministic.
- **Use Case**: Useful for tooling, testing transaction flows, and learning how Ethereum transactions are structured.
- **Best Practice**: Always verify nonces, gas usage, and sign transactions securely when working with real wallets.
