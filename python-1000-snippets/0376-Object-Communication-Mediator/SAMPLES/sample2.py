# sample2.py
# Mediator managing registration and broadcasting of events

class ChatMediator:
    def __init__(self):
        self.participants = []

    def register(self, participant):
        self.participants.append(participant)
        participant.mediator = self

    def broadcast(self, message, sender):
        for participant in self.participants:
            if participant != sender:
                participant.receive(message)


class Participant:
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def send(self, message):
        self.mediator.broadcast(f"{self.name}: {message}", self)

    def receive(self, message):
        print(message)


def main():
    mediator = ChatMediator()
    alice = Participant("Alice")
    bob = Participant("Bob")
    mediator.register(alice)
    mediator.register(bob)
    alice.send("Hi Bob")
    bob.send("Hello Alice")


if __name__ == "__main__":
    main()
