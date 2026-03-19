# Web3 Smart Contract Interaction

## Description
Demonstrates interacting with smart contracts using `web3.py` and a local in-memory Ethereum node (`eth-tester`).

## Requirements
- Python 3.8+
- `web3` (`pip install web3`)
- `py-solc-x` (`pip install py-solc-x`)

## Samples
- `SAMPLES/sample1.py`: Deploy a contract and call a function.
- `SAMPLES/sample2.py`: Sign and send a raw transaction.
- `SAMPLES/sample3.py`: Create an event filter and read logs.

## Running
```bash
python python-1000-snippets/0439-Web3-Smart-Contract-Interaction/SAMPLES/sample1.py
python python-1000-snippets/0439-Web3-Smart-Contract-Interaction/SAMPLES/sample2.py
python python-1000-snippets/0439-Web3-Smart-Contract-Interaction/SAMPLES/sample3.py
```

## Notes
- `eth-tester` provides a local EVM for testing; it does not connect to real networks.
- For production, configure `Web3` with a real provider (Infura, Alchemy, etc.).
