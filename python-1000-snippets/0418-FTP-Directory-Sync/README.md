# FTP Directory Sync

## Description
Demonstrates using a local FTP server (via `pyftpdlib`) and the standard `ftplib` client to sync files between directories.

## Requirements
- Python 3.8+
- `pyftpdlib` (`pip install pyftpdlib`)

## Code (excerpt)
```python
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Start a local FTP server which serves a local directory
authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "./ftp_root", perm="elradfmwMT")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("127.0.0.1", 2121), handler)
```

## Output (sample)
```
Downloaded content: Hello from FTP server
```

## Notes
- The sample scripts start an FTP server on a random free port and shut it down when done.
- For production use, use secure protocols (FTPS/SFTP) and proper authentication.
