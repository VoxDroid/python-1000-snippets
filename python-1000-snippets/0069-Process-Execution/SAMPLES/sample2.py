# sample2.py
# Execute a non-existent command to show error handling

import subprocess

if __name__ == '__main__':
    try:
        subprocess.run(['nonexistentcmd'], check=True)
    except FileNotFoundError:
        print('command not found')
    except subprocess.CalledProcessError:
        print('command failed with non-zero exit')
