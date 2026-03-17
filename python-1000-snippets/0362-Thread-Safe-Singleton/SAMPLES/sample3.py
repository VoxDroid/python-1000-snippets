# sample3.py
# Singleton with lazy initialization and state

import threading


class Config:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
            return cls._instance

    def initialize(self, value):
        if not self._initialized:
            self.value = value
            self._initialized = True


def main():
    c1 = Config()
    c1.initialize("first")
    c2 = Config()
    print("same instance:", c1 is c2)
    print("value:", c2.value)


if __name__ == "__main__":
    main()
