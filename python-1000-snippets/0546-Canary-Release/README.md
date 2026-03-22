# Canary Release

## Description
This snippet demonstrates canary release routing and verification of traffic split.

## Samples
- `SAMPLES/sample1.py`: route single request using a default canary rate (10%).
- `SAMPLES/sample2.py`: compute canary/stable counts for 1000 requests.
- `SAMPLES/sample3.py`: persist canary run stats to `temp/0546_canary.txt`.

## Output
- Example print: `Route: stable` or `Route: canary`.
- `SAMPLES/sample2.py`: stats dictionary.
- File `temp/0546_canary.txt` is written.

## Explanation
Canary release gradually shifts traffic to new code paths. Use this to validate stability before full rollout.
