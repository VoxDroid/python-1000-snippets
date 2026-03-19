# Blockchain Transaction Validation

## Description
This snippet demonstrates signing and validating blockchain transactions using `web3` and `eth_account`.

## Requirements
- Python 3.8+
- `web3` (`pip install web3`)

## Samples
- `SAMPLES/sample1.py`: Sign a transaction and recover the sender address from the signature.
- `SAMPLES/sample2.py`: Show that modifying a transaction changes the signature hash.
- `SAMPLES/sample3.py`: Demonstrate that signatures correspond to specific private keys.

## Running
```bash
python python-1000-snippets/0434-Blockchain-Transaction-Validation/SAMPLES/sample1.py
python python-1000-snippets/0434-Blockchain-Transaction-Validation/SAMPLES/sample2.py
python python-1000-snippets/0434-Blockchain-Transaction-Validation/SAMPLES/sample3.py
```

## Notes
- These examples use local signing only; transactions are not broadcast to an actual network.
- In practice, transactions also include chain-specific fields like `chainId` and `nonce`.
