# 0226-SSH-Client Cheatsheet

* Use `paramiko` for SSH connections in Python.
* Create a `SSHClient` and set `set_missing_host_key_policy(paramiko.AutoAddPolicy())` for testing.
* Connect with `client.connect(host, port, username, pkey=private_key)`.
* Run a command with `exec_command()` and read `stdout`/`stderr`.
* Use `client.open_sftp()` to transfer files or list directories remotely.
* Always validate host keys in production environments.
