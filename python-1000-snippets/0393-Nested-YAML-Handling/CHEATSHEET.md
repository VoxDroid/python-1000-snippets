
# 0393-Nested-YAML-Handling Cheatsheet

- Install `pyyaml` with `pip install pyyaml`.
- Use `yaml.safe_load()` to parse YAML safely.
- Use `yaml.safe_dump()` to serialize Python objects to YAML.
- Beware of YAML's support for complex Python objects (avoid `yaml.load`).
