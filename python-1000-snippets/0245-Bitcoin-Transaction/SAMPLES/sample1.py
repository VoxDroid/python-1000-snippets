# sample1.py
# Generate a deterministic testnet keypair and display the derived address.

from bit import PrivateKeyTestnet

# This fixed WIF is for demo only (do NOT use in production).
FIXED_WIF = 'cUwXNUYgnzph6sRYwuDDr11fNDb84j2DKsTWjjwzWvTRDzuF4TAb'


def main():
    key = PrivateKeyTestnet(FIXED_WIF)
    print('WIF:', key.to_wif())
    print('Address:', key.address)
    print('Public key (hex):', key.public_key.hex())
    print('Compressed:', key.is_compressed())


if __name__ == '__main__':
    main()
