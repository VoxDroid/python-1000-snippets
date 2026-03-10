# 0193-YAML-Parsing Cheatsheet

* Install `pyyaml` for YAML support (`pip install pyyaml`).
* Load: `yaml.safe_load(stream)`; dump: `yaml.safe_dump(obj)`.
* Use `yaml.full_load` only with trusted input.
* Work with files: `yaml.safe_load(open('file.yaml'))` or `yaml.safe_dump(obj, f)`.
* Handle lists, dicts, and custom tags carefully.

