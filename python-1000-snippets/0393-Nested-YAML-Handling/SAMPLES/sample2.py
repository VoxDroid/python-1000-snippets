
# sample2.py
# Parse nested YAML from a temporary file.

import tempfile

try:
    import yaml  # type: ignore
except ImportError:
    print("pyyaml not installed; install with `pip install pyyaml`")
else:
    yaml_text = """
    app:
      name: sample
      components:
        - name: database
          type: postgres
        - name: cache
          type: redis
    """
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".yml", delete=False) as f:
        f.write(yaml_text)
        path = f.name

    data = yaml.safe_load(open(path, "r"))
    print("Loaded YAML from:", path)
    print(data)
