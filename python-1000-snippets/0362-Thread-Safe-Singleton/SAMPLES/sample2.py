# sample2.py
# Demonstrate singleton behavior under thread contention

import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance


def create_instance(instances, index):
    instances[index] = Singleton()


def main():
    instances = [None] * 10
    threads = [threading.Thread(target=create_instance, args=(instances, i)) for i in range(10)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("All same:", all(inst is instances[0] for inst in instances))


if __name__ == "__main__":
    main()
