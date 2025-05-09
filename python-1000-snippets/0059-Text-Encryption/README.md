# Text Encryption

## Description
This snippet implements a simple Caesar cipher to encrypt text by shifting each letter by a fixed number of positions in the alphabet.

## Code
```python
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_base + shift) % 26 + ascii_base)
        else:
            result += char
    return result

text = input("Enter text to encrypt: ")
shift = int(input("Enter shift value: "))
encrypted = encrypt(text, shift)
print("Encrypted text:", encrypted)
```

## Output
```
Enter text to encrypt: Hello, World!
Enter shift value: 3
Encrypted text: Khoor, Zruog!
```

## Explanation
- **Caesar Cipher**: Shifts each letter by `shift` positions (e.g., `A` with shift 3 becomes `D`).
- **Logic**: Preserves case and non-letters; uses modulo (`% 26`) to wrap around the alphabet.
- **Use Case**: Demonstrates basic cryptography; used in educational exercises or puzzles.
- **Limitations**: Not secure for real encryption; easily broken via frequency analysis.
- **Best Practice**: Validate inputs and use secure libraries (e.g., `cryptography`) for real encryption.