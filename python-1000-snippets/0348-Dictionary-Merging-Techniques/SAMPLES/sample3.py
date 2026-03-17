# sample3.py
# Layered configuration using ChainMap

from collections import ChainMap


def main():
    defaults = {"timeout": 30, "retries": 3}
    env = {"timeout": 10}
    user = {"retries": 5}

    config = ChainMap(user, env, defaults)
    print("config:", dict(config))
    print("timeout:", config["timeout"])
    print("retries:", config["retries"])


if __name__ == "__main__":
    main()
