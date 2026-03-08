# sample2.py
# adapting a dict to an object interface

class DictAdapter:
    def __init__(self, d):
        self._d = d
    def get(self, key):
        return self._d.get(key)
    def set(self, key, val):
        self._d[key] = val

if __name__ == '__main__':
    data = {'x': 1}
    obj = DictAdapter(data)
    print(obj.get('x'))
    obj.set('y', 2)
    print(data)  
