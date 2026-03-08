# sample3.py
# Read lines from stdin and output encrypted versions

import sys

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
    shift = int(input('Shift: '))
    print('Encrypting lines:')
    for line in sys.stdin:
        print(encrypt(line.rstrip('\n'), shift))
