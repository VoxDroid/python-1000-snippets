# sample2.py
# Generate and validate an RS256-signed JWT using an RSA key pair.

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import jwt
import time


def generate_rsa_keypair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key


def main():
    private_key, public_key = generate_rsa_keypair()

    # Export keys as PEM (optional; useful for storing or sharing)
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    print('Private key (PEM):')
    print(private_pem.decode().strip())
    print('Public key (PEM):')
    print(public_pem.decode().strip())

    payload = {
        'sub': 'user456',
        'role': 'user',
        'iat': int(time.time()),
        'exp': int(time.time()) + 120,
    }

    token = jwt.encode(payload, private_pem, algorithm='RS256')
    print('JWT:', token)

    decoded = jwt.decode(token, public_pem, algorithms=['RS256'])
    print('Decoded claims:', decoded)


if __name__ == '__main__':
    main()
