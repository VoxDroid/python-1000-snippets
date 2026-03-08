# sample1.py
# Run echo command and capture output

import subprocess

if __name__ == '__main__':
    res = subprocess.run(['echo', 'hello world'], capture_output=True, text=True)
    print('output:', res.stdout.strip())
