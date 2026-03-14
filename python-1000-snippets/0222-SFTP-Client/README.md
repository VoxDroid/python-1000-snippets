# SFTP Client

## Description
This snippet demonstrates an SFTP client using `paramiko` to upload/download files via a local OpenSSH SFTP server.

## Setup
This repository includes a helper directory `.ssh_test/` (next to the `python-1000-snippets` package root) containing:
- A generated SSH keypair (`user_rsa`/`user_rsa.pub`)
- An `sshd_config` configured to listen on `localhost:2222` and use the key for authentication

You can start the SFTP server with:

```bash
sudo sshd -f python-1000-snippets/.ssh_test/sshd_config
```

Then run the samples in `python-1000-snippets/0222-SFTP-Client/SAMPLES/`.

## Code
```python
# Note: Requires `paramiko`. Install with `pip install paramiko`
try:
    import paramiko
    transport = paramiko.Transport(("localhost", 2222))
    # Use key-based auth
    key = paramiko.RSAKey.from_private_key_file(".ssh_test/user_rsa")
    transport.connect(username="vox", pkey=key)
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
File uploaded
```

## Explanation
- **SFTP Client**: Uploads a file to an SFTP server using `paramiko`.
- **Logic**: Connects via SSH, then uses the SFTP subsystem to transfer files.
- **Complexity**: O(n) for transferring n bytes.
- **Use Case**: Secure file transfers between systems.
- **Best Practice**: Use SSH keys, secure the server, and handle errors.
