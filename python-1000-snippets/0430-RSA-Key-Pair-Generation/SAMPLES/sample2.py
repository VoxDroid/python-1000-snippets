# sample2.py
# Load an RSA key pair from PEM files, sign a message, and verify the signature.

import os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


def sign_message(private_key_path: str, message: bytes) -> bytes:
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )
    return signature


def verify_signature(public_key_path: str, message: bytes, signature: bytes) -> bool:
    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

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
    os.makedirs("temp", exist_ok=True)
    priv_path = os.path.join("temp", "rsa_private.pem")
    pub_path = os.path.join("temp", "rsa_public.pem")

    if not (os.path.exists(priv_path) and os.path.exists(pub_path)):
        print("Key files not found; run sample1.py first to generate them.")
        return

    message = b"Message to sign"
    signature = sign_message(priv_path, message)

    print("Message:", message)
    print("Signature (hex):", signature.hex())
    print("Signature valid:", verify_signature(pub_path, message, signature))


if __name__ == "__main__":
    main()
