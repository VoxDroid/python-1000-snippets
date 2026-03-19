# Smart Contract Deployment

## Description
Shows how to compile, deploy, and interact with a smart contract using `web3` and `eth-tester` (an in-memory Ethereum client).

## Requirements
- Python 3.8+
- `web3` (`pip install web3`)
- `py-solc-x` (`pip install py-solc-x`)

## Samples
- `SAMPLES/sample1.py`: Compile and deploy a simple contract.
- `SAMPLES/sample2.py`: Call contract functions to set and read state.
- `SAMPLES/sample3.py`: Emit and read contract events.

## Running
```bash
python python-1000-snippets/0436-Smart-Contract-Deployment/SAMPLES/sample1.py
python python-1000-snippets/0436-Smart-Contract-Deployment/SAMPLES/sample2.py
python python-1000-snippets/0436-Smart-Contract-Deployment/SAMPLES/sample3.py
```

## Notes
- `eth-tester` provides a fast, in-memory blockchain for testing.
- For production, connect to a real Ethereum node (e.g., Infura, Alchemy).
