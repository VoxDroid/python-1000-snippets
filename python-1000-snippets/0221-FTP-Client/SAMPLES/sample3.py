# sample3.py
# Demonstrate directory listing and cleanup via FTP in a local test server.
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
    root = os.path.join(os.getcwd(), 'temp', 'ftp_root3')
    os.makedirs(root, exist_ok=True)
    with open(os.path.join(root, 'test.txt'), 'w') as f:
        f.write('FTP list test')

    server = start_ftp_server(root)
    try:
        ftp = FTP()
        ftp.connect('127.0.0.1', 2121, timeout=5)
        ftp.login('user', 'pass')
        files = ftp.nlst()
        print('Directory listing:', files)
        ftp.quit()
    except all_errors as e:
        print('FTP error:', e)
    finally:
        server.close_all()

