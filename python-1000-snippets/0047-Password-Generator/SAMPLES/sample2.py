# sample2.py
# Generate a password using secrets for cryptographic randomness

import secrets
import string

def secure_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__ == '__main__':
    length = int(input('Length: '))
    print('Secure password:', secure_password(length))
