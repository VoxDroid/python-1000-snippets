# sample1.py
# Basic adapter converting old interface to new interface

class OldSystem:
    def old_request(self):
        return "Old response"


class NewSystemInterface:
    def new_request(self):
        raise NotImplementedError


class Adapter(NewSystemInterface):
    def __init__(self, old):
        self.old = old

    def new_request(self):
        return self.old.old_request()


def main():
    old = OldSystem()
    adapter = Adapter(old)
    print(adapter.new_request())


if __name__ == "__main__":
    main()
