# sample3.py
# EC Diffie-Hellman key agreement (ECIES-like) with AES-GCM encryption.

import os

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def derive_shared_key(private_key, peer_public_key) -> bytes:
    shared_secret = private_key.exchange(ec.ECDH(), peer_public_key)
    # Derive a symmetric key from the shared secret
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'ecdh key agreement',
    )
    return hkdf.derive(shared_secret)


def main():
    # Party A key pair
    a_private = ec.generate_private_key(ec.SECP256R1())
    a_public = a_private.public_key()

    # Party B key pair
    b_private = ec.generate_private_key(ec.SECP256R1())
    b_public = b_private.public_key()

    # Derive shared symmetric keys (should be equal)
    a_key = derive_shared_key(a_private, b_public)
    b_key = derive_shared_key(b_private, a_public)

    assert a_key == b_key

    aesgcm = AESGCM(a_key)
    nonce = os.urandom(12)
    plaintext = b'This message is protected by ECDH-derived key.'

    ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data=None)

    print('Nonce (hex):', nonce.hex())
    print('Ciphertext (hex):', ciphertext.hex())

    # Receiver decrypts with derived key
    decrypted = AESGCM(b_key).decrypt(nonce, ciphertext, associated_data=None)
    print('Decrypted:', decrypted)


if __name__ == '__main__':
    main()
