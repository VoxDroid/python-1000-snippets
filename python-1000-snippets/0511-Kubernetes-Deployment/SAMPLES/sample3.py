# sample3.py
# Check if kubectl exists and optionally run `kubectl version`.

import subprocess


def kubectl_version():
    try:
        output = subprocess.check_output(['kubectl', 'version', '--client', '--short'], stderr=subprocess.STDOUT, timeout=10)
        return output.decode().strip()
    except FileNotFoundError:
        return 'kubectl not installed'
    except subprocess.CalledProcessError as e:
        return 'kubectl command failed: ' + e.output.decode().strip()
    except subprocess.TimeoutExpired:
        return 'kubectl command timed out'


if __name__ == '__main__':
    print(kubectl_version())
