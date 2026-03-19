# sample1.py
# Generate a new Bitcoin private key and derive a P2PKH address.

import hashlib
import secrets

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58_encode(data: bytes) -> str:
    num = int.from_bytes(data, "big")
    encode = ""
    while num > 0:
        num, rem = divmod(num, 58)
        encode = BASE58_ALPHABET[rem] + encode
    # preserve leading zeros
    for b in data:
        if b == 0:
            encode = "1" + encode
        else:
            break
    return encode


def checksum(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()[:4]


def pubkey_to_p2pkh_address(pubkey_bytes: bytes, mainnet: bool = True) -> str:
    sha256_hash = hashlib.sha256(pubkey_bytes).digest()
    ripemd_hash = hashlib.new("ripemd160", sha256_hash).digest()
    prefix = b"\x00" if mainnet else b"\x6f"
    payload = prefix + ripemd_hash
    return base58_encode(payload + checksum(payload))


def generate_keypair() -> tuple[bytes, str]:
    # Generate secp256k1 keypair
    priv_key = ec.generate_private_key(ec.SECP256K1())
    pub_key = priv_key.public_key()
    compressed_pub = pub_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.CompressedPoint,
    )

    priv_bytes = priv_key.private_numbers().private_value.to_bytes(32, "big")
    address = pubkey_to_p2pkh_address(compressed_pub, mainnet=True)
    return priv_bytes, address


def main() -> None:
    priv_bytes, address = generate_keypair()
    print("Generated Bitcoin address (P2PKH):", address)
    print("Private key (hex):", priv_bytes.hex())


if __name__ == "__main__":
    main()
