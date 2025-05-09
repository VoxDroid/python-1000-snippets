# Process Execution

## Description
This snippet executes a system command using the `subprocess` module, capturing its output.

## Code
```python
import subprocess

try:
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
    print("Command output:\n", result.stdout)
except FileNotFoundError:
    print("Command not found.")
except subprocess.CalledProcessError:
    print("Command failed.")
```

## Output
*(On a Unix-like system with files):*
```
Command output:
total 8
-rw-r--r-- 1 user user 123 May  8 14:30 file1.txt
drwxr-xr-x 2 user user 4096 May  8 14:30 folder1
```

## Explanation
- **subprocess.run()**: Executes a command (`ls -l`) and captures output.
- **Arguments**: `capture_output=True` stores stdout/stderr; `text=True` returns strings.
- **Use Case**: Process execution is used for running shell commands, scripts, or external tools.
- **Error Handling**: Catches missing commands or execution failures.
- **Best Practice**: Avoid shell=True for security; validate commands to prevent injection.