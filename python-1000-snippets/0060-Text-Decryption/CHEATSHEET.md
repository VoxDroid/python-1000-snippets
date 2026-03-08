# Text Decryption Cheatsheet

## Decrypt function
def decrypt(text, shift):
    # subtract shift instead of add

## Brute force
```
for s in range(26):
    print(s, decrypt(cipher, s))
```

## Tips
- Decryption is symmetrical with encryption (use negative shift too).
- Useful when shift is unknown; human-readable output indicates correct guess.

## Running samples
Activate venv and run `SAMPLES/sample*.py`.
