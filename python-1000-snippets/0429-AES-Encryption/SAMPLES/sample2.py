# sample2.py
# Demonstrates AES-GCM encryption using cryptography's AESGCM class.

import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def main() -> None:
    key = AESGCM.generate_key(bit_length=128)
    aesgcm = AESGCM(key)

    nonce = os.urandom(12)
    plaintext = b"Secret data to encrypt"
    associated_data = b"auth-data"

    ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data)
    print("Key:", key)
    print("Nonce:", nonce)
    print("Ciphertext:", ciphertext)

    decrypted = aesgcm.decrypt(nonce, ciphertext, associated_data)
    print("Decrypted:", decrypted)


if __name__ == "__main__":
    main()
