# sample1.py
# Demonstrates encrypting and decrypting data using Fernet (AES-128-GCM under the hood).

from cryptography.fernet import Fernet


def main() -> None:
    key = Fernet.generate_key()
    cipher = Fernet(key)

    plaintext = b"Secret message"
    token = cipher.encrypt(plaintext)

    print("Key (base64):", key)
    print("Encrypted token:", token)

    decrypted = cipher.decrypt(token)
    print("Decrypted text:", decrypted)


if __name__ == "__main__":
    main()
