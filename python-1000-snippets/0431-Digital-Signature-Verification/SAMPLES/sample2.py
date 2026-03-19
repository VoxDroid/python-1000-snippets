# sample2.py
# Demonstrates signature verification failure when the message is tampered with.

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def generate_rsa_keypair():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def sign_message(private_key, message: bytes) -> bytes:
    return private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )


def verify_signature(public_key, message: bytes, signature: bytes) -> bool:
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        return True
    except Exception:
        return False


def main() -> None:
    priv = generate_rsa_keypair()
    pub = priv.public_key()

    original = b"Original message"
    signature = sign_message(priv, original)

    tampered = b"Tampered message"

    print("Original signature valid:", verify_signature(pub, original, signature))
    print("Tampered message valid:", verify_signature(pub, tampered, signature))


if __name__ == "__main__":
    main()
