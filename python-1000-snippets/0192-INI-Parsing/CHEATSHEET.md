# 0192-INI-Parsing Cheatsheet

* Parse INI from string: `config.read_string(text)`.
* Use `config.sections()` and `config.items(section)` to iterate.
* Access with interpolation: `%(other)s` and defaults.
* Use `config.get(section, option, fallback=val)` to avoid KeyError.
* Read from file or file-like object with `read_file()`.
* Write changes with `config.write()`.

