# sample2.py
# Validate an email address using regex

import re

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if __name__ == '__main__':
    email = input('Email: ')
    if re.match(pattern, email):
        print(email, 'is valid')
    else:
        print(email, 'is invalid')
