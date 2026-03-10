# sample3.py
import configparser

cfg = configparser.ConfigParser()
cfg.read_dict({'defaults': {'x':'10'}})
print('x default:', cfg.get('defaults','x'))

