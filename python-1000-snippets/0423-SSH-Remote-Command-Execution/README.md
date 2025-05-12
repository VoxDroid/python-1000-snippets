# SSH Remote Command Execution

## Description
This snippet demonstrates executing a remote command via SSH using `paramiko`.

## Code
```python
# Note: Requires `paramiko`. Install with `pip install paramiko`
try:
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect("localhost", username="user", password="pass")
    stdin, stdout, stderr = client.exec_command("echo Hello")
    print(stdout.read().decode())
    client.close()
except ImportError:
    print("Mock Output: Hello")
```

## Output
```
Mock Output: Hello
```
*(Real output with `paramiko` and SSH server: `Hello`)*

## Explanation
- **SSH Remote Command Execution**: Runs a command on a remote server.
- **Logic**: Uses `paramiko` to execute `echo Hello` via SSH.
- **Complexity**: O(1) per command (network-dependent).
- **Use Case**: Used for server automation or management.
- **Best Practice**: Use key-based auth; handle errors; secure connections.