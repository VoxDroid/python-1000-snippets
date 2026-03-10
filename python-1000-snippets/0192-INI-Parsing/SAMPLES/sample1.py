# sample1.py
import configparser

ini = """
[one]
a=1
[two]
b=2
"""
cfg = configparser.ConfigParser()
cfg.read_string(ini)
print(cfg.sections())
print('a in one:', cfg['one']['a'])

