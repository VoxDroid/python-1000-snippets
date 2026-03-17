# sample2.py
# Instantiating an abstract class raises TypeError

from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def foo(self):
        pass


def main():
    try:
        Base()
    except TypeError as e:
        print("error:", e)


if __name__ == "__main__":
    main()
