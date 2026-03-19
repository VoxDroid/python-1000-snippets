# sample2.py
# Generate a WIF from a private key and decode it to verify the resulting address.

import hashlib

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
BASE58_ALPHABET_INDEX = {c: i for i, c in enumerate(BASE58_ALPHABET)}


def base58_encode(data: bytes) -> str:
    num = int.from_bytes(data, "big")
    encode = ""
    while num > 0:
        num, rem = divmod(num, 58)
        encode = BASE58_ALPHABET[rem] + encode
    # preserve leading zero bytes (base58 '1')
    for b in data:
        if b == 0:
            encode = "1" + encode
        else:
            break
    return encode


def base58_decode(value: str) -> bytes:
    num = 0
    for char in value:
        num = num * 58 + BASE58_ALPHABET_INDEX[char]
    combined = num.to_bytes((num.bit_length() + 7) // 8, "big")
    n_pad = 0
    for c in value:
        if c == "1":
            n_pad += 1
        else:
            break
    return b"\x00" * n_pad + combined


def checksum(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()[:4]


def privkey_to_wif(priv_bytes: bytes, compressed: bool = True, mainnet: bool = True) -> str:
    prefix = b"\x80" if mainnet else b"\xef"
    payload = prefix + priv_bytes + (b"\x01" if compressed else b"")
    return base58_encode(payload + checksum(payload))


def wif_to_private_key(wif: str) -> bytes:
    decoded = base58_decode(wif)
    payload, check = decoded[:-4], decoded[-4:]
    if checksum(payload) != check:
        raise ValueError("Invalid WIF checksum")

    # Remove prefix and optional compression suffix
    return payload[1:33]


def pubkey_to_p2pkh_address(pubkey_bytes: bytes, mainnet: bool = True) -> str:
    sha256_hash = hashlib.sha256(pubkey_bytes).digest()
    ripemd_hash = hashlib.new("ripemd160", sha256_hash).digest()
    prefix = b"\x00" if mainnet else b"\x6f"
    payload = prefix + ripemd_hash
    return base58_encode(payload + checksum(payload))


def main() -> None:
    # Use a deterministic private key for reproducible output.
    priv_bytes = bytes.fromhex("11" * 32)
    wif = privkey_to_wif(priv_bytes, compressed=True, mainnet=True)

    decoded_priv = wif_to_private_key(wif)
    assert decoded_priv == priv_bytes, "WIF decode mismatch"

    private_key = ec.derive_private_key(int.from_bytes(decoded_priv, "big"), ec.SECP256K1())
    public_key = private_key.public_key()
    compressed_pub = public_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.CompressedPoint,
    )

    address = pubkey_to_p2pkh_address(compressed_pub, mainnet=True)

    print("WIF:", wif)
    print("Derived address:", address)


if __name__ == "__main__":
    main()
