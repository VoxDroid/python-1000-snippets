# sample1.py
# Hash and verify a password using bcrypt.

import bcrypt


def main():
    password = b'super-secure-password'

    # Hash the password (includes salt)
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    print('Hashed (bcrypt):', hashed)

    # Verify the password
    valid = bcrypt.checkpw(password, hashed)
    print('Password verified:', valid)

    # Wrong password should not verify
    print('Wrong password verified:', bcrypt.checkpw(b'wrong-password', hashed))


if __name__ == '__main__':
    main()
