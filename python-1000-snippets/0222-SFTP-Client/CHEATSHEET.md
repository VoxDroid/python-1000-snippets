# 0222-SFTP-Client Cheatsheet

* Install `paramiko` with `pip install paramiko`.
* Use `paramiko.Transport((host, port))` to connect, then `Transport.connect(username=..., password=...)`.
* Create an SFTP client: `sftp = paramiko.SFTPClient.from_transport(transport)`.
* Upload file: `sftp.put(localpath, remotepath)`.
* Download file: `sftp.get(remotepath, localpath)`.
* Close: `sftp.close()` and `transport.close()`.
* For key-based auth use `paramiko.RSAKey.from_private_key_file(...)` and `transport.connect(pkey=... )`.
* Handle exceptions like `paramiko.SSHException` and `socket.error`.
* For testing, you can run an in-process SSH/SFTP server using `paramiko.ServerInterface`.
* Use secure passwords and restrict `SFTPServerInterface` operations as needed.

