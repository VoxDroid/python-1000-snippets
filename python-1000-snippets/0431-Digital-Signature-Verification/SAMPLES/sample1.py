# sample1.py
# Demonstrates signing and verifying messages using RSA and SHA256.

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

    message = b"Verify me"
    signature = sign_message(priv, message)

    print("Message:", message)
    print("Signature (hex):", signature.hex())
    print("Signature valid:", verify_signature(pub, message, signature))


if __name__ == "__main__":
    main()
