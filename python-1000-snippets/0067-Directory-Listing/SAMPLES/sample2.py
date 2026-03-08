# sample2.py
# Recursively list files and directories

import os

if __name__ == '__main__':
    for root, dirs, files in os.walk('.'):
        print('Root:', root)
        for d in dirs:
            print('  dir:', d)
        for f in files:
            print('  file:', f)
