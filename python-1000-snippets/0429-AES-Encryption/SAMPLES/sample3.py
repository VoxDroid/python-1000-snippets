# sample3.py
# Demonstrates AES-CBC encryption/decryption with PKCS7 padding using cryptography.

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


def encrypt(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    padder = padding.PKCS7(128).padder()
    padded = padder.update(plaintext) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(padded) + encryptor.finalize()


def decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded) + unpadder.finalize()


def main() -> None:
    key = os.urandom(32)  # AES-256
    iv = os.urandom(16)
    plaintext = b"Confidential payload"

    ciphertext = encrypt(plaintext, key, iv)
    print("Key:", key)
    print("IV:", iv)
    print("Ciphertext:", ciphertext)

    decrypted = decrypt(ciphertext, key, iv)
    print("Decrypted:", decrypted)


if __name__ == "__main__":
    main()
