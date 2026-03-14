# sample2.py
# Download a file from a local FTP server created on the fly.
import os
import threading
from ftplib import FTP, all_errors

from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer


def start_ftp_server(ftp_root, user='user', password='pass', port=2121):
    authorizer = DummyAuthorizer()
    authorizer.add_user(user, password, ftp_root, perm='elradfmw')
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer(('127.0.0.1', port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


if __name__ == '__main__':
    root = os.path.join(os.getcwd(), 'temp', 'ftp_root2')
    os.makedirs(root, exist_ok=True)
    local_file = os.path.join(root, 'remote.txt')
    with open(local_file, 'w') as f:
        f.write('FTP download test')

    server = start_ftp_server(root)
    try:
        ftp = FTP()
        ftp.connect('127.0.0.1', 2121, timeout=5)
        ftp.login('user', 'pass')
        with open(os.path.join(root, 'downloaded.txt'), 'wb') as f:
            ftp.retrbinary('RETR remote.txt', f.write)
        ftp.quit()
        print('Downloaded file content:', open(os.path.join(root, 'downloaded.txt')).read())
    except all_errors as e:
        print('FTP error:', e)
    finally:
        server.close_all()

