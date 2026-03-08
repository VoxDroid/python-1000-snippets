# sample2.py
# Decrypt by negating shift and show round-trip

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

if __name__ == '__main__':
    original = "Secret Message!"
    shifted = encrypt(original, 10)
    print('shifted:', shifted)
    print('restored:', encrypt(shifted, -10))
