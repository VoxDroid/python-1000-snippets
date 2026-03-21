# sample2.py
# List currently running docker containers (if available).

import subprocess


def list_containers():
    try:
        out = subprocess.check_output(['docker', 'ps', '--format', '{{.ID}} {{.Image}} {{.Status}}'], stderr=subprocess.STDOUT, timeout=20)
        lines = out.decode().strip().splitlines()
        print('Running containers (count=', len(lines), '):')
        for line in lines:
            print(' ', line)
    except FileNotFoundError:
        print('Docker CLI not available')
    except subprocess.CalledProcessError as e:
        print('Docker ps failed:', e.output.decode().strip())
    except subprocess.TimeoutExpired:
        print('Docker ps timed out')


if __name__ == '__main__':
    list_containers()
