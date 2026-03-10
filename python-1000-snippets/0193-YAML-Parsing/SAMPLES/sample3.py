# sample3.py
try:
    import yaml
    print('loaded:', yaml.safe_load('a: 1'))
except ImportError:
    print('Mock Output: a=1')

