# sample1.py
# Parse a hard-coded JSON string and access fields

import json

if __name__ == '__main__':
    s = '{"name": "Alice", "age": 30, "hobbies": ["reading", "gaming"]}'
    data = json.loads(s)
    print('parsed:', data)
    print('name field:', data['name'])
    print('first hobby:', data['hobbies'][0])
