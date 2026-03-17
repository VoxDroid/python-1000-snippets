# sample3.py
# Thread-safe virtual proxy with lazy initialization

import threading


class ExpensiveResource:
    def __init__(self):
        self.value = "initialized"


class ThreadSafeProxy:
    def __init__(self):
        self._resource = None
        self._lock = threading.Lock()

    def get(self):
        if self._resource is None:
            with self._lock:
                if self._resource is None:
                    self._resource = ExpensiveResource()
        return self._resource


def main():
    proxy = ThreadSafeProxy()
    resource = proxy.get()
    print(resource.value)


if __name__ == "__main__":
    main()
