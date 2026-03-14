# sample2.py
# Symmetric encryption using AES-GCM with cryptography primitives.

import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def main():
    key = AESGCM.generate_key(bit_length=256)
    aesgcm = AESGCM(key)

    nonce = os.urandom(12)
    plaintext = b'Confidential message'

    ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data=None)

    print('Key (hex):', key.hex())
    print('Nonce (hex):', nonce.hex())
    print('Ciphertext (hex):', ciphertext.hex())

    decrypted = aesgcm.decrypt(nonce, ciphertext, associated_data=None)
    print('Decrypted:', decrypted)


if __name__ == '__main__':
    main()
