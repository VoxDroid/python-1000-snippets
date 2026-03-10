# sample2.py
try:
    import yaml
    obj = {'list': [1,2,3]}
    with open('out.yaml','w') as f:
        yaml.safe_dump(obj, f)
    print('dumped to out.yaml')
except ImportError:
    print('cannot write, missing pyyaml')

