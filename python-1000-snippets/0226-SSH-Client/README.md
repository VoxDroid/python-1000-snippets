# SSH Client

## Description
This snippet demonstrates using `paramiko` to execute commands and transfer files over SSH.

## Setup
A local OpenSSH server is available in `.ssh_test/` (see the SFTP snippet). It listens on `localhost:2222` and is configured for key-based authentication.

## Code
```python
# Run the sample scripts in python-1000-snippets/0226-SSH-Client/SAMPLES/
```

## Output
The samples print the output of remote commands or the results of SFTP directory listings.

## Explanation
- **Paramiko**: A Python SSH library for executing commands, transferring files, and more.
- **Logic**: Establish an SSH connection with a private key, then run commands or open SFTP sessions.
- **Use Case**: Automating remote administration, file transfers, or command execution.
- **Best Practice**: Use key-based auth, validate host keys, and avoid hardcoding credentials.
