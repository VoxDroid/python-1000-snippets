# sample1.py
# Use a local OpenSSH server (localhost:2222) with key-based auth to upload/download a file.
#
# Note: The repository includes a helper folder at `.ssh_test/` with generated keys
# and a minimal sshd_config for running a local OpenSSH server for testing.
import os

import paramiko


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SSH_TEST_DIR = os.path.join(REPO_ROOT, '.ssh_test')


def get_key_path():
    # Generated in .ssh_test by setup outside the snippet.
    return os.path.join(SSH_TEST_DIR, 'user_rsa')


if __name__ == '__main__':
    key_path = get_key_path()
    if not os.path.exists(key_path):
        print('SFTP key not found, cannot run sample. Generate keys in .ssh_test in the repo.')
        exit(0)

    try:
        key = paramiko.RSAKey.from_private_key_file(key_path)
        transport = paramiko.Transport(('127.0.0.1', 2222))
        transport.connect(username=os.getlogin(), pkey=key)
        sftp = paramiko.SFTPClient.from_transport(transport)

        temp_dir = os.path.join(os.getcwd(), 'temp', 'sftp_client')
        os.makedirs(temp_dir, exist_ok=True)
        local_file = os.path.join(temp_dir, 'upload.txt')
        with open(local_file, 'w') as f:
            f.write('Hello, SFTP!')

        remote = 'upload.txt'
        sftp.put(local_file, remote)
        print('Uploaded file to remote:', remote)

        downloaded = os.path.join(temp_dir, 'downloaded.txt')
        sftp.get(remote, downloaded)
        print('Downloaded content:', open(downloaded).read())

        sftp.close()
        transport.close()
    except Exception as e:
        print('SFTP error:', e)

