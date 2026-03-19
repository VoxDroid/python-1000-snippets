# NFT Metadata Creation

## Description
Demonstrates creating and hashing NFT metadata in the standard JSON format.

## Requirements
- Python 3.8+

## Samples
- `SAMPLES/sample1.py`: Create basic NFT metadata JSON.
- `SAMPLES/sample2.py`: Compute a deterministic hash from metadata (useful for IPFS/CID generation).
- `SAMPLES/sample3.py`: Save metadata to a file and compute its hash.

## Running
```bash
python python-1000-snippets/0438-NFT-Metadata-Creation/SAMPLES/sample1.py
python python-1000-snippets/0438-NFT-Metadata-Creation/SAMPLES/sample2.py
python python-1000-snippets/0438-NFT-Metadata-Creation/SAMPLES/sample3.py
```

## Notes
- Consistent JSON serialization (sorted keys, stable separators) is important for hashing.
- IPFS CIDs are commonly used to reference NFT metadata; you can compute them from the file content.
