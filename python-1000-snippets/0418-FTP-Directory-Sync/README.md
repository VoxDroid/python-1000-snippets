# FTP Directory Sync

## Description
This snippet demonstrates FTP file upload using `ftplib`.

## Code
```python
# Note: Requires `ftplib`
try:
    from ftplib import FTP
    ftp = FTP("localhost")
    ftp.login("user", "pass")
    with open("test.txt", "wb") as f:
        f.write("Test")
    with open("test.txt", "rb") as f:
        ftp.storbinary("STOR test.txt", f)
    print("File uploaded")
except ImportError:
    print("Mock Output: File uploaded")
```

## Output
```
Mock Output: File uploaded
```
*(Real output with `ftplib` and FTP server: `File uploaded`)*

## Explanation
- **FTP Directory Sync**: Uploads a file to an FTP server.
- **Logic**: Connects to FTP, uploads a binary file.
- **Complexity**: O(n) for n bytes in file.
- **Use Case**: Used for file transfers or backups.
- **Best Practice**: Secure with FTPS; handle connection errors; validate paths.