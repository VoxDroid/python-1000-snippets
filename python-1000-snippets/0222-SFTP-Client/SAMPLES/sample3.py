# sample3.py
# Remove a file on a local OpenSSH SFTP server using a private key.
#
# Note: This sample assumes a local OpenSSH server is running on localhost:2222
# and that the keypair is stored under `.ssh_test/` in the repo.
import os

import paramiko


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SSH_TEST_DIR = os.path.join(REPO_ROOT, '.ssh_test')


def get_key_path():
    return os.path.join(SSH_TEST_DIR, 'user_rsa')


if __name__ == '__main__':
    key_path = get_key_path()
    if not os.path.exists(key_path):
        print('SFTP key not found; generate keys in .ssh_test in the repo.')
        exit(0)

    try:
        key = paramiko.RSAKey.from_private_key_file(key_path)
        transport = paramiko.Transport(('127.0.0.1', 2222))
        transport.connect(username=os.getlogin(), pkey=key)
        sftp = paramiko.SFTPClient.from_transport(transport)

        remote_file = 'to_delete.txt'
        try:
            sftp.remove(remote_file)
            print('Removed', remote_file)
        except IOError as e:
            print('Could not remove', remote_file, '-', e)

        print('Remote list:', sftp.listdir('.'))
        sftp.close()
        transport.close()
    except Exception as e:
        print('SFTP error:', e)

