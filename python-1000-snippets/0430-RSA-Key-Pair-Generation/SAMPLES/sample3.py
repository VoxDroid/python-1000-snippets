# sample3.py
# Demonstrates RSA encryption/decryption (OAEP) using generated key pair.

import os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


def encrypt_message(public_key_path: str, message: bytes) -> bytes:
    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    return public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )


def decrypt_message(private_key_path: str, ciphertext: bytes) -> bytes:
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    return private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )


def main() -> None:
    os.makedirs("temp", exist_ok=True)
    priv_path = os.path.join("temp", "rsa_private.pem")
    pub_path = os.path.join("temp", "rsa_public.pem")

    if not (os.path.exists(priv_path) and os.path.exists(pub_path)):
        print("Key files not found; run sample1.py first to generate them.")
        return

    plaintext = b"Secret message"
    ciphertext = encrypt_message(pub_path, plaintext)
    print("Ciphertext (hex):", ciphertext.hex())

    decrypted = decrypt_message(priv_path, ciphertext)
    print("Decrypted:", decrypted)


if __name__ == "__main__":
    main()
