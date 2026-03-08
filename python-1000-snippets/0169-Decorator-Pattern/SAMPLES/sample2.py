# sample2.py
# add notification behavior to a user object

class User:
    def notify(self, msg):
        print('user received', msg)

class NotifierDecorator:
    def __init__(self, user):
        self._user = user
    def notify(self, msg):
        print('sending email')
        self._user.notify(msg)

if __name__ == '__main__':
    u = User()
    u2 = NotifierDecorator(u)
    u2.notify('hello')
