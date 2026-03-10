# sample1.py
# read configuration file

import configparser

config = configparser.ConfigParser()
config['Database'] = {'host': 'localhost', 'port': '5432'}

with open('settings.ini', 'w') as f:
    config.write(f)

# read it back
cfg = configparser.ConfigParser()
cfg.read('settings.ini')
print('DB Host:', cfg['Database']['host'])
