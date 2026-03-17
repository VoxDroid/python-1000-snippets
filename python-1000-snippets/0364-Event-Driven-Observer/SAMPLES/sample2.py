# sample2.py
# Observer pattern with remove/unsubscribe support

class Observer:
    def update(self, message):
        print(f"Received: {message}")


class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers = [o for o in self.observers if o is not observer]

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


def main():
    subject = Subject()
    o1 = Observer()
    o2 = Observer()
    subject.add_observer(o1)
    subject.add_observer(o2)
    subject.notify("first")

    subject.remove_observer(o1)
    subject.notify("second")


if __name__ == "__main__":
    main()
