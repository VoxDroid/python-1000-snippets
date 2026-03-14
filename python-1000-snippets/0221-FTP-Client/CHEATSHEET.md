# 0221-FTP-Client Cheatsheet

* Use the standard library `ftplib` for FTP operations.
* Connect: `ftp = FTP(host)` and `ftp.login(user, passwd)`.
* Upload files: `ftp.storbinary('STOR filename', open('local', 'rb'))`.
* Download files: `ftp.retrbinary('RETR filename', callback)`.
* List directory: `ftp.nlst()` or `ftp.dir()`.
* Change directory: `ftp.cwd(path)`.
* Use passive mode: `ftp.set_pasv(True)` (default), disable with `set_pasv(False)`.
* Close connection: `ftp.quit()`.
* Handle network errors: catch `ftplib.all_errors`.
* For secure transfers, use `ftplib.FTP_TLS` (FTPS).
* Example: start a local FTP server with `pyftpdlib` for testing.

