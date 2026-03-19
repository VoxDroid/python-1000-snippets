# sample1.py
# Demonstrates signing a message with secp256k1 and deriving an Ethereum-style address.

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature
from eth_utils import keccak


def generate_key():
    return ec.generate_private_key(ec.SECP256K1())


def eth_address_from_public_key(public_key) -> str:
    # Ethereum address is last 20 bytes of keccak-256 of uncompressed public key.
    public_numbers = public_key.public_numbers()
    x = public_numbers.x.to_bytes(32, "big")
    y = public_numbers.y.to_bytes(32, "big")
    uncompressed = b"\x04" + x + y
    addr = keccak(uncompressed)[-20:]
    return "0x" + addr.hex()


def main() -> None:
    key = generate_key()
    pub = key.public_key()
    addr = eth_address_from_public_key(pub)

    message = b"Hello, blockchain!"
    signature = key.sign(message, ec.ECDSA(hashes.SHA256()))
    r, s = decode_dss_signature(signature)

    print("Address:", addr)
    print("Message:", message)
    print("Signature (r,s):", (r, s))


if __name__ == "__main__":
    main()
