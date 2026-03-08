# JSON Parsing Cheatsheet

## Loading
- `json.loads(s)` parse string
- `json.load(fp)` parse file

## Dumping
- `json.dumps(obj)` serialize to string
- `json.dump(obj, fp)` write to file

## Tips
- Use `indent` argument for pretty-print.
- Beware of trailing commas (invalid JSON).

## Example
```python
data = json.loads('{"key":1}')
print(data['key'])
```

## Running samples
Activate venv then run `SAMPLES/sample*.py`.
