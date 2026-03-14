# sample2.py
# Hybrid encryption: encrypt data with AES-GCM and wrap the AES key with RSA-OAEP.

import os

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes


def main():
    # Generate RSA key pair for key wrapping
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Generate a random AES key and nonce
    aes_key = AESGCM.generate_key(bit_length=256)
    aesgcm = AESGCM(aes_key)
    nonce = os.urandom(12)

    plaintext = b'Hybrid encryption is useful for large payloads.'

    # Encrypt the data with AES-GCM
    ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data=None)

    # Wrap (encrypt) the AES key with RSA-OAEP
    wrapped_key = public_key.encrypt(
        aes_key,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
    )

    print('Wrapped AES key (hex):', wrapped_key.hex())
    print('Nonce (hex):', nonce.hex())
    print('Ciphertext (hex):', ciphertext.hex())

    # Unwrap AES key and decrypt
    unwrapped_key = private_key.decrypt(
        wrapped_key,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
    )

    decrypted = AESGCM(unwrapped_key).decrypt(nonce, ciphertext, associated_data=None)
    print('Decrypted:', decrypted)


if __name__ == '__main__':
    main()
