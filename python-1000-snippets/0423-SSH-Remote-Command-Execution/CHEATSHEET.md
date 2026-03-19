# 0423 - SSH Remote Command Execution Cheatsheet

## Quick Facts
- Uses `asyncssh` to start an in-process SSH server and run client commands.
- Demonstrates running commands, capturing stdout/stderr, and streaming output.

## Run Samples
```bash
python python-1000-snippets/0423-SSH-Remote-Command-Execution/SAMPLES/sample1.py
python python-1000-snippets/0423-SSH-Remote-Command-Execution/SAMPLES/sample2.py
python python-1000-snippets/0423-SSH-Remote-Command-Execution/SAMPLES/sample3.py
```

## Key asyncssh APIs
- `asyncssh.create_server(...)` - start an SSH server.
- `asyncssh.connect(...)` - connect as an SSH client.
- `conn.run(command)` - run a command and get stdout/stderr.
- `conn.create_process(command)` - run a command and stream output.

## Notes
- The server in these examples uses simple password auth (`user`/`12345`).
- In real deployments, use key-based auth and proper host key verification (`known_hosts`).
