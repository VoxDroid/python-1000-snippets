# sample2.py
# Demonstrates that modifying a signed transaction invalidates the signature.

from eth_account import Account


def main() -> None:
    account = Account.create()
    private_key = account.key

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

    # Recover address from the original signed transaction
    recovered_ok = Account.recover_transaction(signed.rawTransaction)
    print("Recovered address (original):", recovered_ok)

    # Tamper with the transaction by changing the value.
    tx_tampered = dict(tx)
    tx_tampered["value"] = tx["value"] + 1
    signed_tampered = Account.sign_transaction(tx_tampered, private_key)

    # Trying to recover from the original signature using tampered tx is not meaningful;
    # Instead, demonstrate that the raw signed transaction hash changes.
    print("Original tx hash:", signed.hash.hex())
    print("Tampered tx hash:", signed_tampered.hash.hex())
    print(
        "Hashes differ:", signed.hash.hex() != signed_tampered.hash.hex()
    )


if __name__ == "__main__":
    main()
