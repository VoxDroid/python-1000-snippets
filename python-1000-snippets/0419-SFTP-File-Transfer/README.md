# SFTP File Transfer

## Description
This snippet demonstrates how to run a local SFTP server and client using `asyncssh`.
It includes examples for:

- Downloading files from an SFTP server (`sample1.py`)
- Uploading files to an SFTP server (`sample2.py`)
- Syncing directories between local and remote (`sample3.py`)

## Requirements
- Python 3.8+
- `asyncssh` (`pip install asyncssh`)

## Quickstart
Run one of the sample scripts:

```bash
python python-1000-snippets/0419-SFTP-File-Transfer/SAMPLES/sample1.py
python python-1000-snippets/0419-SFTP-File-Transfer/SAMPLES/sample2.py
python python-1000-snippets/0419-SFTP-File-Transfer/SAMPLES/sample3.py
```

## Sample Output (sample1)
```
SFTP server listening on port 12345
Remote files: ['.', '..', 'hello.txt']
Downloaded content: Hello from SFTP server
```

## Notes
- The samples launch an in-process SFTP server (no external service required).
- `asyncssh` requires host key configuration; here we generate an in-memory key for demo purposes.
- For production, use key-based authentication, host key verification, and secure credential storage.
