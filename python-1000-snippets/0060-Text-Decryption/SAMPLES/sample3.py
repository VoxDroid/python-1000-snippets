# sample3.py
# Read encrypted text and shift from stdin then decrypt

import sys

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

if __name__ == '__main__':
    shift = int(input('Shift: '))
    text = sys.stdin.read().strip()
    print(decrypt(text, shift))
