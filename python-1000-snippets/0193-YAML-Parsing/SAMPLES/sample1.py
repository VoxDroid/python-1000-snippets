# sample1.py
try:
    import yaml
    data = yaml.safe_load('key: value')
    print(data)
except ImportError:
    print('PyYAML not available')

