
# 0392-Complex-INI-Processing Cheatsheet

- Use `configparser.ConfigParser()` to read INI files.
- `config.sections()` lists the sections.
- Use `config.get(section, option)` or `config[section][option]`.
- Write INI files with `config.write(fileobj)`.
- Use `configparser.ExtendedInterpolation()` for value interpolation.
