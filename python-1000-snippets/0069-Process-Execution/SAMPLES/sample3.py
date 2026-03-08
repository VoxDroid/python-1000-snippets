# sample3.py
# Build a safe command from user input and execute

import subprocess
import shlex

if __name__ == '__main__':
    cmd = input('Command: ')
    args = shlex.split(cmd)
    result = subprocess.run(args, capture_output=True, text=True)
    print(result.stdout)
