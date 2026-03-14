# sample3.py
# Symmetric encryption using AES-CBC with PKCS7 padding.

import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def pad(data: bytes, block_size: int = 128) -> bytes:
    padder = padding.PKCS7(block_size).padder()
    return padder.update(data) + padder.finalize()


def unpad(padded: bytes, block_size: int = 128) -> bytes:
    unpadder = padding.PKCS7(block_size).unpadder()
    return unpadder.update(padded) + unpadder.finalize()


def main():
    key = os.urandom(32)
    iv = os.urandom(16)
    plaintext = b'Important secret message'

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padded = pad(plaintext)
    ciphertext = encryptor.update(padded) + encryptor.finalize()

    print('Key (hex):', key.hex())
    print('IV (hex):', iv.hex())
    print('Ciphertext (hex):', ciphertext.hex())

    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    decrypted = unpad(decrypted_padded)

    print('Decrypted:', decrypted)


if __name__ == '__main__':
    main()
