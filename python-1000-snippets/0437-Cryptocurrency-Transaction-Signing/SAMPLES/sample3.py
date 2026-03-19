# sample3.py
# Demonstrates recovering an Ethereum-style address from an ECDSA signature.

from eth_keys import keys
from eth_utils import keccak


def main() -> None:
    private_key = keys.PrivateKey(keccak(b"seed"))
    public_key = private_key.public_key
    address = public_key.to_checksum_address()

    message = b"Recover me"
    message_hash = keccak(message)

    signature = private_key.sign_msg_hash(message_hash)
    recovered_pk = signature.recover_public_key_from_msg_hash(message_hash)
    recovered_address = recovered_pk.to_checksum_address()

    print("Original address:", address)
    print("Recovered address:", recovered_address)
    print("Addresses match:", address == recovered_address)


if __name__ == "__main__":
    main()
