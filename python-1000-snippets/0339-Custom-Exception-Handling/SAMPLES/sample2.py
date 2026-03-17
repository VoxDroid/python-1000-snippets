"""Parse and validate a config dictionary, raising custom errors."""

from typing import Any, Dict


class ConfigError(Exception):
    pass


def validate_config(config: Dict[str, Any]) -> None:
    required_keys = ["host", "port", "timeout"]
    for key in required_keys:
        if key not in config:
            raise ConfigError(f"Missing required key '{key}'")
    if not isinstance(config["port"], int):
        raise ConfigError("Port must be an integer")


if __name__ == "__main__":
    config = {"host": "localhost", "port": "not-an-int"}
    try:
        validate_config(config)
        print("Config valid")
    except ConfigError as e:
        print("Config error:", str(e))
