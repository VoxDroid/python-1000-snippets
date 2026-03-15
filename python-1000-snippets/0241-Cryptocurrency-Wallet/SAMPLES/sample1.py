# sample1.py
# Generate a Bitcoin Testnet wallet keypair and print address details.

from bit import PrivateKeyTestnet

# Use a fixed private key for reproducible output (do NOT use in production).
FIXED_WIF = 'cUwXNUYgnzph6sRYwuDDr11fNDb84j2DKsTWjjwzWvTRDzuF4TAb'

if __name__ == '__main__':
    key = PrivateKeyTestnet(FIXED_WIF)
    print('Private key (WIF):', key.to_wif())
    print('Address:', key.address)
    print('Public key (hex):', key.public_key.hex())
    print('Is compressed:', key.is_compressed())
    print('Network: testnet')
