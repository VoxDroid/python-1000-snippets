# sample1.py
# Create a temporary source file and copy it to destination

import shutil

if __name__ == '__main__':
    src = 'source1.txt'
    dst = 'dest1.txt'
    with open(src, 'w') as f:
        f.write('hello world')
    try:
        shutil.copy(src, dst)
        print('copied', src, 'to', dst)
    except Exception as e:
        print('error', e)
