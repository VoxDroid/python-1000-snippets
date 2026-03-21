# sample1.py
# Try launching a minimal container command via docker CLI.

import subprocess


def run_hello():
    try:
        out = subprocess.check_output(['docker', 'run', '--rm', 'alpine', 'echo', 'hello'], stderr=subprocess.STDOUT, timeout=20)
        print('Container output:', out.decode().strip())
    except FileNotFoundError:
        print('Docker CLI not available')
    except subprocess.CalledProcessError as e:
        print('Docker command failed', e.output.decode().strip())
    except subprocess.TimeoutExpired:
        print('Docker command timed out')


if __name__ == '__main__':
    run_hello()
