# sample1.py
# Symmetric encryption using Fernet (AES-128-GCM with authentication).

from cryptography.fernet import Fernet


def main():
    key = Fernet.generate_key()
    cipher = Fernet(key)

    plaintext = b'Hello, World!'
    token = cipher.encrypt(plaintext)

    print('Key:', key)
    print('Ciphertext:', token)

    decrypted = cipher.decrypt(token)
    print('Decrypted:', decrypted)


if __name__ == '__main__':
    main()
