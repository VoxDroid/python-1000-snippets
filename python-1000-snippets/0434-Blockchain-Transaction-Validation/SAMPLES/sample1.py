# sample1.py
# Demonstrates signing an Ethereum transaction and validating its signature.

from eth_account import Account
from eth_account.messages import encode_defunct


def main() -> None:
    # Generate a random private key (for demo purposes only).
    account = Account.create()
    private_key = account.key
    address = account.address

    print("Account address:", address)

    # A simple transaction payload (not broadcasted).
    tx = {
        "nonce": 0,
        "gasPrice": 1_000_000_000,
        "gas": 21000,
        "to": "0x0000000000000000000000000000000000000000",
        "value": 1_000_000_000_000_000,
        "data": b"",
        "chainId": 1,
    }

    signed = Account.sign_transaction(tx, private_key)
    print("Signed transaction hash:", signed.hash.hex())
    print("Signature components:", signed.v, signed.r, signed.s)

    # Recover address from signed transaction
    recovered = Account.recover_transaction(signed.rawTransaction)
    print("Recovered address:", recovered)
    print("Signature valid:", recovered.lower() == address.lower())


if __name__ == "__main__":
    main()
