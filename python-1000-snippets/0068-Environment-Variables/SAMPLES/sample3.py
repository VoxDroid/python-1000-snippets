# sample3.py
# List environment variables starting with a given prefix

import os

if __name__ == '__main__':
    prefix = input('Prefix: ')
    for k,v in os.environ.items():
        if k.startswith(prefix):
            print(k, '=', v)
