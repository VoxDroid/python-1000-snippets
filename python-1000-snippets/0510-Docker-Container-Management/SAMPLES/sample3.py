# sample3.py
# Log docker availability check into temp/0510_docker_status.txt.

import os
import subprocess

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0510_docker_status.txt')


def check_docker():
    try:
        out = subprocess.check_output(['docker', '--version'], stderr=subprocess.STDOUT, timeout=10)
        return out.decode().strip()
    except FileNotFoundError:
        return 'Docker CLI not installed'
    except subprocess.CalledProcessError as e:
        return f'Docker check failed: {e.output.decode().strip()}'
    except subprocess.TimeoutExpired:
        return 'Docker check timed out'


if __name__ == '__main__':
    status = check_docker()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(status + '\n')
    print('Wrote Docker status to', OUTPUT_PATH)
