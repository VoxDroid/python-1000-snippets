# sample3.py
# Try to run `docker ps` to verify container runtime availability.

import subprocess


if __name__ == '__main__':
    try:
        out = subprocess.check_output(['docker', 'ps', '--format', '{{.Names}}']).decode().strip()
        print('Docker containers:', out if out else '(none)')
    except FileNotFoundError:
        print('Docker CLI not installed; skipping runtime check')
    except subprocess.CalledProcessError as e:
        print('Docker command failed:', e)
