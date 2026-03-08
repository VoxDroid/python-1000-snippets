# sample2.py
# Delete all .tmp files in current directory

import os
import glob

if __name__ == '__main__':
    for fname in glob.glob('*.tmp'):
        try:
            os.remove(fname)
            print('removed', fname)
        except Exception as e:
            print('failed to remove', fname, e)
