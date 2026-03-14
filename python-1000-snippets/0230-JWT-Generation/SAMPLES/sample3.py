# sample3.py
# Generate and validate an ES256 JWT (ECDSA) with a custom header.

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
import jwt
import time


def generate_ec_keypair():
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()
    return private_key, public_key


def main():
    private_key, public_key = generate_ec_keypair()

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
        'sub': 'user789',
        'role': 'viewer',
        'iat': int(time.time()),
        'exp': int(time.time()) + 90,
    }

    headers = {'kid': 'example-key-id'}

    token = jwt.encode(payload, private_pem, algorithm='ES256', headers=headers)
    print('JWT:', token)

    decoded = jwt.decode(token, public_pem, algorithms=['ES256'])
    print('Decoded claims:', decoded)


if __name__ == '__main__':
    main()
