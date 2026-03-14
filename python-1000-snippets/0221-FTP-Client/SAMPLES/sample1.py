# sample1.py
# Start a local FTP server and upload a file to it using ftplib.
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
    root = os.path.join(os.getcwd(), 'temp', 'ftp_root')
    os.makedirs(root, exist_ok=True)

    server = start_ftp_server(root)
    try:
        ftp = FTP()
        ftp.connect('127.0.0.1', 2121, timeout=5)
        ftp.login('user', 'pass')

        local_path = os.path.join(root, 'upload.txt')
        with open(local_path, 'w') as f:
            f.write('Hello, FTP!')

        with open(local_path, 'rb') as f:
            ftp.storbinary('STOR upload.txt', f)
        print('File uploaded')
        ftp.quit()
    except all_errors as e:
        print('FTP error:', e)
    finally:
        server.close_all()

