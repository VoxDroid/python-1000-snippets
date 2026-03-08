# sample3.py
# Write an object to a file as JSON and read it back

import json

if __name__ == '__main__':
    obj = {'x': 1, 'y': 2}
    fname = 'data.json'
    with open(fname, 'w') as f:
        json.dump(obj, f)
    print('wrote', fname)
    with open(fname) as f:
        loaded = json.load(f)
    print('loaded object:', loaded)
