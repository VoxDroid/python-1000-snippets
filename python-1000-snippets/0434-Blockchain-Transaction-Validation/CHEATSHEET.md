# 0434-Blockchain-Transaction-Validation Cheatsheet

- Use `eth_account` from `web3` to sign and recover transaction sender addresses.
- The signed transaction includes `v,r,s` values and can be serialized to raw bytes.

## Sign a transaction
```py
from eth_account import Account
signed = Account.sign_transaction(tx, private_key)
```

## Recover sender from signed transaction
```py
sender = Account.recover_transaction(signed.rawTransaction)
```

## Notes
- Signed transactions are valid only for the exact payload; changing any field changes the signature.
- In real-world use, you must manage nonces and gas prices for the target chain.
