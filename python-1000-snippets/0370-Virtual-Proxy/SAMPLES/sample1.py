# sample1.py
# Virtual proxy for lazy initialization of an expensive object

class RealSubject:
    def __init__(self):
        # Simulate expensive initialization
        self._data = "Real data"

    def request(self):
        return self._data


class Proxy:
    def __init__(self):
        self._real = None

    def request(self):
        if self._real is None:
            self._real = RealSubject()
        return self._real.request()


def main():
    proxy = Proxy()
    print(proxy.request())


if __name__ == "__main__":
    main()
