# sample1.py
import json
data = {"name": "Alice", "age": 30}
js = json.dumps(data)
print("JSON:", js)
print("Parsed:", json.loads(js))

