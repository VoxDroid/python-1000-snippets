# SSH Client

## Description
This snippet demonstrates an SSH client using `paramiko` to execute a remote command.

## Code
```python
# Note: Requires `paramiko`. Install with `pip install paramiko`
try:
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect("localhost", username="user", password="password")
    stdin, stdout, stderr = client.exec_command("echo Hello")
    print("Output:", stdout.read().decode().strip())
    client.close()
except ImportError:
    print("Mock Output: Output: Hello")
```

## Output
```
Mock Output: Output: Hello
```
*(Real output with SSH: `Output: Hello`)*

## Explanation
- **SSH Client**: Executes a command on a remote server using `paramiko`.
- **Logic**: Connects, runs `echo Hello`, and reads the output.
- **Complexity**: O(1) for command execution (network latency varies).
- **Use Case**: Used for remote server management or automation.
- **Best Practice**: Use SSH keys; handle errors; ensure server is accessible.