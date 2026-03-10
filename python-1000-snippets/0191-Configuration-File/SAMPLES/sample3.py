# sample3.py
# use fallback values when options are missing

import configparser

cfg = configparser.ConfigParser()
cfg.read('settings.ini')
timeout = cfg.get('Database', 'timeout', fallback='30')
print('Timeout:', timeout)
