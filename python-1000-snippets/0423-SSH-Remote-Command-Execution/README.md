# SSH Remote Command Execution

## Description
This snippet demonstrates executing remote commands over SSH using `asyncssh`.

Each example runs an in-process SSH server and connects to it, so no external SSH host is required.

## Requirements
- Python 3.8+
- `asyncssh` (`pip install asyncssh`)

## Samples
- `SAMPLES/sample1.py`: Run a simple command and print stdout.
- `SAMPLES/sample2.py`: Run a command that fails and print stderr/exit code.
- `SAMPLES/sample3.py`: Stream command output line-by-line.

## Running
```bash
python python-1000-snippets/0423-SSH-Remote-Command-Execution/SAMPLES/sample1.py
python python-1000-snippets/0423-SSH-Remote-Command-Execution/SAMPLES/sample2.py
python python-1000-snippets/0423-SSH-Remote-Command-Execution/SAMPLES/sample3.py
```

## Notes
- These examples use password-based authentication for simplicity (user: `user`, password: `12345`).
- For production, prefer key-based authentication and proper host key verification.
