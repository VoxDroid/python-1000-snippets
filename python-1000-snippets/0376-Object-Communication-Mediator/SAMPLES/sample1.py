# sample1.py
# Basic mediator relaying messages between components

class Mediator:
    def notify(self, sender, event):
        pass


class ConcreteMediator(Mediator):
    def __init__(self):
        self.components = []

    def add(self, component):
        self.components.append(component)

    def notify(self, sender, event):
        for component in self.components:
            if component != sender:
                component.receive(event)


class Component:
    def __init__(self, mediator):
        self.mediator = mediator

    def send(self, event):
        self.mediator.notify(self, event)

    def receive(self, event):
        print(f"Received: {event}")


def main():
    mediator = ConcreteMediator()
    c1 = Component(mediator)
    c2 = Component(mediator)
    mediator.add(c1)
    mediator.add(c2)
    c1.send("Hello")


if __name__ == "__main__":
    main()
