# sample3.py
# Build and sign a raw Bitcoin transaction using a constructed UTXO.

from bit import PrivateKeyTestnet
from bit.network.meta import Unspent

FIXED_WIF = 'cUwXNUYgnzph6sRYwuDDr11fNDb84j2DKsTWjjwzWvTRDzuF4TAb'


def main():
    key = PrivateKeyTestnet(FIXED_WIF)

    # Construct a fake UTXO (for offline signing; not broadcast).
    utxo = Unspent(
        amount=500_000,  # sats (0.005 BTC)
        confirmations=1,
        script=key.scriptcode,
        txid='00' * 32,
        txindex=0,
    )

    # Send 0.001 BTC to another address (here using the same key as recipient).
    outputs = [(key.address, 100_000, 'satoshi')]

    raw_tx = key.create_transaction(outputs, fee=1_000, unspents=[utxo])
    print('Raw transaction (hex):', raw_tx)

    # Derive txid from raw transaction (double SHA256, little-endian)
    import hashlib

    raw_bytes = bytes.fromhex(raw_tx)
    txid = hashlib.sha256(hashlib.sha256(raw_bytes).digest()).digest()[::-1].hex()
    print('TxID (derived):', txid)


if __name__ == '__main__':
    main()
