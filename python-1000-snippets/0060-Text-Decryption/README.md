# Text Decryption

## Description
This snippet decrypts text encrypted with a Caesar cipher by shifting letters back by the same number of positions used for encryption.

## Code
```python
def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_base - shift) % 26 + ascii_base)
        else:
            result += char
    return result

text = input("Enter text to decrypt: ")
shift = int(input("Enter shift value: "))
decrypted = decrypt(text, shift)
print("Decrypted text:", decrypted)
```

## Output
```
Enter text to decrypt: Khoor, Zruog!
Enter shift value: 3
Decrypted text: Hello, World!
```

## Explanation
- **Caesar Cipher Decryption**: Reverses encryption by shifting backward (subtracting `shift`).
- **Logic**: Same as encryption but subtracts `shift` instead of adding; preserves case and non-letters.
- **Use Case**: Complements the encryption snippet; used in educational exercises.
- **Limitations**: Assumes correct shift value; not secure for real-world use.
- **Best Practice**: Pair with encryption snippet and validate inputs for robustness.