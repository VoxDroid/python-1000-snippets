# SFTP File Transfer

## Description
This snippet demonstrates SFTP file upload using `paramiko`.

## Code
```python
# Note: Requires `paramiko`. Install with `pip install paramiko`
try:
    import paramiko
    transport = paramiko.Transport(("localhost", 22))
    transport.connect(username="user", password="pass")
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put("local.txt", "remote.txt")
    sftp.close()
    transport.close()
    print("File transferred")
except ImportError:
    print("Mock Output: File transferred")
```

## Output
```
Mock Output: File transferred
```
*(Real output with `paramiko` and SFTP server: `File transferred`)*

## Explanation
- **SFTP File Transfer**: Uploads a file via SFTP.
- **Logic**: Uses `paramiko` to securely transfer a file.
- **Complexity**: O(n) for n bytes in file.
- **Use Case**: Used for secure file transfers.
- **Best Practice**: Use key-based auth; handle errors; validate paths.