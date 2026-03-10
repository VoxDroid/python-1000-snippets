# sample2.py
import configparser

cfg = configparser.ConfigParser()
cfg['two'] = {'b': '2'}
with open('temp.ini', 'w') as f:
    cfg.write(f)

cfg2 = configparser.ConfigParser()
cfg2.read('temp.ini')
print('sections:', cfg2.sections())

