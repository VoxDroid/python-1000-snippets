# sample3.py
# Copy a file and then rename the destination

import shutil
import os

if __name__ == '__main__':
    src = 'source1.txt'
    dst = 'dest1.txt'
    newname = 'dest_renamed.txt'
    if os.path.exists(src):
        shutil.copy(src, dst)
        os.rename(dst, newname)
        print('copied and renamed to', newname)
    else:
        print('source missing', src)
