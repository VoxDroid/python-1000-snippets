# sample2.py
# List directory contents over SFTP using Paramiko.

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
    with paramiko.Transport(('127.0.0.1', 2222)) as transport:
        transport.connect(username='vox', pkey=key)
        with paramiko.SFTPClient.from_transport(transport) as sftp:
            print('Remote home directory listing:')
            for name in sftp.listdir('.'):  # list home directory
                print(' -', name)
