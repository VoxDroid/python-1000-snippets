# sample3.py
# Filter for files with a given extension

import os

if __name__ == '__main__':
    ext = input('extension (e.g. .py): ')
    matches = [f for f in os.listdir('.') if f.endswith(ext)]
    print('matched:', matches)
