# sample1.py
# Execute a command on a local SSH server using Paramiko.

import os

import paramiko


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SSH_TEST_DIR = os.path.join(REPO_ROOT, '.ssh_test')


def get_key_path():
    return os.path.join(SSH_TEST_DIR, 'user_rsa')


if __name__ == '__main__':
    key_path = get_key_path()
    if not os.path.exists(key_path):
        print('SSH key not found at', key_path)
        exit(0)

    key = paramiko.RSAKey.from_private_key_file(key_path)
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('127.0.0.1', port=2222, username='vox', pkey=key)
        stdin, stdout, stderr = client.exec_command('uname -a')
        print('STDOUT:', stdout.read().decode().strip())
        print('STDERR:', stderr.read().decode().strip())
        client.close()
