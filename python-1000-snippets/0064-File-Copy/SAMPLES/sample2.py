# sample2.py
# Copy all .txt files in the current directory to a backup folder

import os
import shutil

if __name__ == '__main__':
    os.makedirs('backup', exist_ok=True)
    for fname in os.listdir('.'):
        if fname.endswith('.txt') and fname.startswith('source1') == False:
            shutil.copy(fname, os.path.join('backup', fname))
            print('backed up', fname)
