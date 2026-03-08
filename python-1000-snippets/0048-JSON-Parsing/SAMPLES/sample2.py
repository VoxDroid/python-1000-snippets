# sample2.py
# Read JSON from stdin and print a requested key

import json
import sys

if __name__ == '__main__':
    print('Enter JSON object:')
    text = sys.stdin.read()
    try:
        data = json.loads(text)
        print('keys:', list(data.keys()))
    except json.JSONDecodeError as e:
        print('JSON error:', e)
