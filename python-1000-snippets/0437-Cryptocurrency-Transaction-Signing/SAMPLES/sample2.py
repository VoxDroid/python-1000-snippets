# sample2.py
# Demonstrates verifying an ECDSA signature and detecting tampering.

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature


def main() -> None:
    key = ec.generate_private_key(ec.SECP256K1())
    pub = key.public_key()

    message = b"Important transaction"
    signature = key.sign(message, ec.ECDSA(hashes.SHA256()))

    try:
        pub.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        print("Signature valid")
    except InvalidSignature:
        print("Signature invalid")

    # Tamper with the message
    tampered = b"Tampered transaction"
    try:
        pub.verify(signature, tampered, ec.ECDSA(hashes.SHA256()))
        print("Tampered message incorrectly verified")
    except InvalidSignature:
        print("Tampered message correctly rejected")


if __name__ == "__main__":
    main()
