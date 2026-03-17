# sample1.py
# Basic thread-safe singleton implementation

import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance


def main():
    s1 = Singleton()
    s2 = Singleton()
    print("same instance:", s1 is s2)


if __name__ == "__main__":
    main()
