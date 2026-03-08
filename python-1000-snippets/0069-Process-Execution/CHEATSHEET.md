# Process Execution Cheatsheet

## subprocess.run
```
res = subprocess.run(['ls','-l'], capture_output=True, text=True)
print(res.stdout)
```

## check_output
```
out = subprocess.check_output(['uname','-a'], text=True)
```

## Popen for advanced use
```
p = subprocess.Popen(['cmd'], stdout=subprocess.PIPE)
out = p.communicate()
```

## Tips
- `res.returncode` indicates success (0) or failure.
- Avoid `shell=True` unless necessary. Use `shlex.split()` to parse strings.

## Running samples
Activate venv and execute the sample scripts.
