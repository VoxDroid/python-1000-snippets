# sample3.py
# Demonstrates using ECDSA (secp256r1) to sign and verify a message.

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec


def generate_ecdsa_keypair():
    return ec.generate_private_key(ec.SECP256R1())


def sign_message(private_key, message: bytes) -> bytes:
    return private_key.sign(message, ec.ECDSA(hashes.SHA256()))


def verify_signature(public_key, message: bytes, signature: bytes) -> bool:
    try:
        public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        return True
    except Exception:
        return False


def main() -> None:
    priv = generate_ecdsa_keypair()
    pub = priv.public_key()

    message = b"ECDSA signing"
    signature = sign_message(priv, message)

    print("Message:", message)
    print("Signature (hex):", signature.hex())
    print("Signature valid:", verify_signature(pub, message, signature))


if __name__ == "__main__":
    main()
