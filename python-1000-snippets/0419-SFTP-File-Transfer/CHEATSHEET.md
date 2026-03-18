# 0419 - SFTP File Transfer Cheatsheet

## Quick Tips
- Use `asyncssh` when you need an in-process Python SFTP server + client.
- Host key verification is disabled in these demos via `known_hosts=None`; **do not** do this in production.
- For real deployments, store host keys in a file and set `known_hosts` to that path.

## Examples
- `sample1.py`: Download a file from the server.
- `sample2.py`: Upload a file to the server.
- `sample3.py`: Sync a local directory with a remote directory (recursive get/put).

## Running
```bash
python python-1000-snippets/0419-SFTP-File-Transfer/SAMPLES/sample1.py
python python-1000-snippets/0419-SFTP-File-Transfer/SAMPLES/sample2.py
python python-1000-snippets/0419-SFTP-File-Transfer/SAMPLES/sample3.py
```

## Key asyncssh APIs
- `asyncssh.create_server(...)` - start an in-memory SSH/SFTP server.
- `asyncssh.connect(...)` - connect as an SSH client.
- `SFTPClient.get(...)` / `SFTPClient.put(...)` - download/upload files and directories.
