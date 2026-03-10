# sample2.py
# chatroom mediator example

class ChatRoom:
    def __init__(self):
        self.users = []
    def register(self, user):
        self.users.append(user)
        user.chatroom = self
    def send(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive(message)

class User:
    def __init__(self, name):
        self.name = name
        self.chatroom = None
    def send(self, msg):
        self.chatroom.send(f"{self.name}: {msg}", self)
    def receive(self, msg):
        print(f"{self.name} got message: {msg}")

if __name__ == '__main__':
    room = ChatRoom()
    u1 = User('Alice')
    u2 = User('Bob')
    room.register(u1)
    room.register(u2)
    u1.send('Hi Bob!')
    u2.send('Hello Alice!')
