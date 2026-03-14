# sample3.py
# Run a remote command via Paramiko and stream its output.

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
        transport = client.get_transport()
        chan = transport.open_session()
        chan.exec_command('echo Hello from remote; sleep 0.1; echo Done')
        while True:
            if chan.recv_ready():
                print('OUT>', chan.recv(1024).decode().strip())
            if chan.recv_stderr_ready():
                print('ERR>', chan.recv_stderr(1024).decode().strip())
            if chan.exit_status_ready():
                break
        print('Exit status:', chan.recv_exit_status())
        chan.close()
