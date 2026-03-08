# Environment Variables Cheatsheet

## Accessing
```
import os
val = os.getenv('HOME', '/tmp')
```
- or `os.environ.get('HOME')`

## Setting
```
os.environ['MYVAR']='value'
```

## Tips
- Changes affect current process and children only.
- Use `del os.environ['VAR']` to remove.

## Example
```
for k,v in os.environ.items():
    if k.startswith('PY'):
        print(k,v)
```

## Running samples
Activate venv and run `SAMPLES/sample*.py`.
