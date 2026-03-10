# 0191-Configuration-File Cheatsheet

* Use `configparser.ConfigParser()` to work with INI-style configuration.
* Read from file: `config.read('path.ini')`.
* Access sections: `config['Section']['key']`.
* Set defaults: `config['DEFAULT']['timeout'] = '30'`.
* Write back: `with open('out.ini','w') as f: config.write(f)`.
* Use `get`, `getint`, `getboolean` with fallback.

