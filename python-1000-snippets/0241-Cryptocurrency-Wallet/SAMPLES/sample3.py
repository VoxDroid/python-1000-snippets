# sample3.py
# Create and sign a raw Bitcoin transaction using a manually provided UTXO.

from bit import PrivateKeyTestnet
from bit.network.meta import Unspent

FIXED_WIF = 'cPpnLSntPyWNW6M3vkVR6c5WYhRgEbknGvXf3ngE1CwPgLbcQ4Ju'

if __name__ == '__main__':
    key = PrivateKeyTestnet(FIXED_WIF)

    # Build a fake UTXO (this is for demonstration; the tx will not be broadcast).
    utxo = Unspent(
        amount=300_000,  # sats (0.003 BTC)
        confirmations=1,
        script=key.scriptcode,
        txid='00' * 32,
        txindex=0,
    )

    # Send 45_000 sats to a recipient (here we use our own address)
    outputs = [(key.address, 45_000, 'satoshi')]

    raw_tx = key.create_transaction(outputs, fee=1_000, unspents=[utxo])
    print('Raw transaction (hex):', raw_tx)

    # Derive txid from raw transaction (double SHA-256, little-endian)
    import hashlib

    raw_bytes = bytes.fromhex(raw_tx)
    txid = hashlib.sha256(hashlib.sha256(raw_bytes).digest()).digest()[::-1].hex()
    print('TxID (derived):', txid)
