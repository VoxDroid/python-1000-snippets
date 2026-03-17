# sample2.py
# Proxy with caching behavior

class DataSource:
    def fetch(self, key):
        return f"value for {key}"


class CacheProxy:
    def __init__(self, source):
        self.source = source
        self.cache = {}

    def get(self, key):
        if key not in self.cache:
            self.cache[key] = self.source.fetch(key)
        return self.cache[key]


def main():
    source = DataSource()
    proxy = CacheProxy(source)
    print(proxy.get("a"))
    print(proxy.get("a"))  # cached


if __name__ == "__main__":
    main()
