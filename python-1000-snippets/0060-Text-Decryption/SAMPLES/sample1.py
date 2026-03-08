# sample1.py
# Decrypt a hardcoded Caesar cipher text with known shift

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_base - shift) % 26 + ascii_base)
        else:
            result += char
    return result

if __name__ == '__main__':
    cipher = "Khoor, Zruog!"
    print('cipher:', cipher)
    print('decrypted:', decrypt(cipher, 3))
