# sample3.py
# Demonstrates verifying a signed transaction with the expected sender address.

from eth_account import Account


def main() -> None:
    sender = Account.create()
    other = Account.create()

    tx = {
        "nonce": 0,
        "gasPrice": 1_000_000_000,
        "gas": 21000,
        "to": "0x0000000000000000000000000000000000000000",
        "value": 1_000_000_000_000_000,
        "data": b"",
        "chainId": 1,
    }

    signed = Account.sign_transaction(tx, sender.key)
    recovered = Account.recover_transaction(signed.rawTransaction)

    print("Sender address:", sender.address)
    print("Recovered address:", recovered)
    print("Signature valid:", recovered.lower() == sender.address.lower())

    # Verify that a signature from a different key yields a different recovered address.
    signed_other = Account.sign_transaction(tx, other.key)
    recovered_other = Account.recover_transaction(signed_other.rawTransaction)
    print("Other signer recovered address:", recovered_other)
    print(
        "Different signer equals sender:",
        recovered_other.lower() == sender.address.lower(),
    )


if __name__ == "__main__":
    main()
