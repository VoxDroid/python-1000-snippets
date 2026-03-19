# sample3.py
# Show difference between mainnet and testnet Bitcoin addresses for the same key.

import hashlib

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58_encode(data: bytes) -> str:
    num = int.from_bytes(data, "big")
    encode = ""
    while num > 0:
        num, rem = divmod(num, 58)
        encode = BASE58_ALPHABET[rem] + encode
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


def main() -> None:
    # Use a fixed private key for deterministic output.
    # 32 bytes of 0x11 (hex) gives a valid secp256k1 private key.
    priv_bytes = bytes.fromhex("11" * 32)
    priv_int = int.from_bytes(priv_bytes, "big")

    priv_key = ec.derive_private_key(priv_int, ec.SECP256K1())
    pub_key = priv_key.public_key()
    compressed_pub = pub_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.CompressedPoint,
    )

    mainnet_addr = pubkey_to_p2pkh_address(compressed_pub, mainnet=True)
    testnet_addr = pubkey_to_p2pkh_address(compressed_pub, mainnet=False)

    print("Mainnet P2PKH address:", mainnet_addr)
    print("Testnet P2PKH address:", testnet_addr)


if __name__ == "__main__":
    main()
