# Digital Signature Verification

## Description
This snippet demonstrates creating and verifying digital signatures using the `cryptography` library.

## Requirements
- Python 3.8+
- `cryptography` (`pip install cryptography`)

## Samples
- `SAMPLES/sample1.py`: Sign a message with RSA and verify the signature.
- `SAMPLES/sample2.py`: Show signature verification failing when the message is altered.
- `SAMPLES/sample3.py`: Sign and verify a message using ECDSA (secp256r1).

## Running
```bash
python python-1000-snippets/0431-Digital-Signature-Verification/SAMPLES/sample1.py
python python-1000-snippets/0431-Digital-Signature-Verification/SAMPLES/sample2.py
python python-1000-snippets/0431-Digital-Signature-Verification/SAMPLES/sample3.py
```

## Notes
- Always verify signatures using the correct public key.
- Use well-established algorithms and avoid custom signature schemes.
