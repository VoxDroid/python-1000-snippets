# sample1.py
# Basic observer pattern implementation

class Observer:
    def update(self, message):
        print(f"Received: {message}")


class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


def main():
    subject = Subject()
    observer = Observer()
    subject.add_observer(observer)
    subject.notify("Event 1")


if __name__ == "__main__":
    main()
