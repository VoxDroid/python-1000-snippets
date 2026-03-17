
# sample1.py
# Parse nested YAML data from a string.

try:
    import yaml  # type: ignore
except ImportError:
    print("pyyaml not installed; install with `pip install pyyaml`")
else:
    yaml_text = """
    parent:
      child1: value1
      child2: value2
    """
    data = yaml.safe_load(yaml_text)
    print("Parsed:", data)
    print("Child1:", data["parent"]["child1"])
