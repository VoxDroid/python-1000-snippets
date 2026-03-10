# sample1.py
# basic mediator example (from README)

class Mediator:
    def __init__(self):
        self.components = []
    def register(self, component):
        self.components.append(component)
    def notify(self, sender, message):
        for component in self.components:
            if component != sender:
                component.receive(message)

class Component:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
    def send(self, message):
        self.mediator.notify(self, f"{self.name}: {message}")
    def receive(self, message):
        print(f"{self.name} received: {message}")

if __name__ == '__main__':
    mediator = Mediator()
    c1 = Component("A", mediator)
    c2 = Component("B", mediator)
    mediator.register(c1)
    mediator.register(c2)
    c1.send("Hello")
