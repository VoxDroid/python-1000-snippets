
            # sample3.py
            # Dump Python objects to YAML.

            try:
                import yaml  # type: ignore
            except ImportError:
                print("pyyaml not installed; install with `pip install pyyaml`")
            else:
                data = {
                    "server": {"host": "localhost", "port": 8080},
                    "features": ["auth", "logging", "metrics"],
                }
                yaml_text = yaml.safe_dump(data, sort_keys=False)
                print("YAML output:
", yaml_text)
