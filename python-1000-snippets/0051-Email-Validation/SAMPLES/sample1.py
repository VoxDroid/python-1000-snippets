# sample1.py
# Prompt for an email address and validate format

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    addr = input('Email: ')
    print(f"{addr} ->", 'valid' if is_valid_email(addr) else 'invalid')
