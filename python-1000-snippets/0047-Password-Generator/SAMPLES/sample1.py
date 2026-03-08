# sample1.py
# Generate a single password using random.choice

import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == '__main__':
    length = int(input('Length: '))
    print('Password:', generate_password(length))
