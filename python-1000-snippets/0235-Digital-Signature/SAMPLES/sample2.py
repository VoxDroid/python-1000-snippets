# sample2.py
# Create and verify an ECDSA signature (secp256r1).

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes


def main():
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()

    message = b'ECDSA signature example'

    signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))
    print('Signature (hex):', signature.hex())

    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print('Signature verified successfully.')


if __name__ == '__main__':
    main()
