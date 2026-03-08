# Text Encryption Cheatsheet

## Caesar cipher function
```python
def encrypt(text, shift):
    # iterate characters
```
```
char.isalpha(), ord('a'), ord('A'), chr()
```

## Shifting logic
- Calculate base depending on case.
- `(ord(char)-base+shift) % 26 + base` ensures wrap-around.

## Tips
- Negative shift decrypts.
- Non-letter characters are preserved.

## Running samples
Activate venv and run each script, piping input into sample3.
