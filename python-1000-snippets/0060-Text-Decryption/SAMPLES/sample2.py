# sample2.py
# Brute-force all shifts to attempt decryption

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
    cipher = "Uijt jt b usbotgftt!"
    for s in range(26):
        print(s, decrypt(cipher, s))
