# sample3.py
# authentication/authorization chain example

class Handler:
    def __init__(self, successor=None):
        self._successor = successor
    def handle(self, request):
        pass

class AuthHandler(Handler):
    def handle(self, request):
        if not request.get('user'):
            return 'Auth failed'
        return self._successor.handle(request) if self._successor else 'OK'

class RoleHandler(Handler):
    def handle(self, request):
        if request.get('role') != 'admin':
            return 'Not authorized'
        return 'Allowed'

if __name__ == '__main__':
    chain = AuthHandler(RoleHandler())
    print(chain.handle({'user': 'alice', 'role': 'admin'}))
    print(chain.handle({'role': 'guest'}))
