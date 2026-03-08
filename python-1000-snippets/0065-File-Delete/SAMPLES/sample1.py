# sample1.py
# Create a temporary file and then delete it

import os

if __name__ == '__main__':
    fname = 'temp_delete.txt'
    with open(fname, 'w') as f:
        f.write('delete me')
    try:
        os.remove(fname)
        print('deleted', fname)
    except Exception as e:
        print('error', e)
