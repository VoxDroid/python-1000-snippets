# sample2.py
# Sign and verify a message using a Bitcoin testnet private key.

from bit import PrivateKeyTestnet

FIXED_WIF = 'cUwXNUYgnzph6sRYwuDDr11fNDb84j2DKsTWjjwzWvTRDzuF4TAb'


def main():
    key = PrivateKeyTestnet(FIXED_WIF)
    message = b"Hello from python-1000-snippets"

    signature = key.sign(message)
    print('Message:', message.decode())
    print('Signature (hex):', signature.hex())

    verified = key.verify(signature, message)
    print('Signature valid:', verified)


if __name__ == '__main__':
    main()
