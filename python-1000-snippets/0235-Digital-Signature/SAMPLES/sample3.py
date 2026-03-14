# sample3.py
# Create and verify an Ed25519 signature.

from cryptography.hazmat.primitives.asymmetric import ed25519


def main():
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    message = b'Ed25519 signature example'

    signature = private_key.sign(message)
    print('Signature (hex):', signature.hex())

    public_key.verify(signature, message)
    print('Signature verified successfully.')


if __name__ == '__main__':
    main()
