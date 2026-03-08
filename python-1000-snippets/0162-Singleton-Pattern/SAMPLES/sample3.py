# sample3.py
# thread-safe singleton with lock

import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

if __name__ == '__main__':
    def create():
        print('created', ThreadSafeSingleton())
    threads = [threading.Thread(target=create) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
