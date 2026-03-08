# sample1.py
# Encrypt a hardcoded string with shift=5

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_base + shift) % 26 + ascii_base)
        else:
            result += char
    return result

if __name__ == '__main__':
    text = "Hello, World!"
    print('original:', text)
    print('encrypted:', encrypt(text, 5))
