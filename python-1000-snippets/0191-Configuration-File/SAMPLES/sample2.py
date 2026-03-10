# sample2.py
# modify configuration file

import configparser

cfg = configparser.ConfigParser()
cfg.read('settings.ini')
cfg['Database']['user'] = 'admin'

with open('settings.ini', 'w') as f:
    cfg.write(f)

print('Updated user:', cfg['Database']['user'])
