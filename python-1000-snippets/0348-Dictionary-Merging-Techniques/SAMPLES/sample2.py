# sample2.py
# Deep merge nested dictionaries

def deep_merge(a, b):
    result = dict(a)
    for k, v in b.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result


def main():
    base = {"db": {"host": "localhost", "port": 5432}, "debug": False}
    override = {"db": {"port": 5433}, "debug": True}
    print("merged:", deep_merge(base, override))


if __name__ == "__main__":
    main()
