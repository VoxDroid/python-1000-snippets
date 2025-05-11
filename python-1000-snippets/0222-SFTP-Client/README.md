# SFTP Client

## Description
This snippet demonstrates an SFTP client using `paramiko` to upload a file.

## Code
```python
# Note: Requires `paramiko`. Install with `pip install paramiko`
try:
    import paramiko
    transport = paramiko.Transport(("localhost", 22))
    transport.connect(username="user", password="password")
    sftp = paramiko.SFTPClient.from_transport(transport)
    with open("test.txt", "w") as f:
        f.write("Hello, SFTP!")
    sftp.put("test.txt", "remote_test.txt")
    print("File uploaded")
    sftp.close()
    transport.close()
except ImportError:
    print("Mock Output: File uploaded")
```

## Output
```
Mock Output: File uploaded
```
*(Real output with SFTP: `File uploaded`)*

## Explanation
- **SFTP Client**: Uploads a file to an SFTP server using `paramiko`.
- **Logic**: Connects, creates a local file, and uploads it with `put`.
- **Complexity**: O(n) for uploading n bytes.
- **Use Case**: Used for secure file transfers in modern systems.
- **Best Practice**: Use SSH keys; handle connection errors; ensure server is running.