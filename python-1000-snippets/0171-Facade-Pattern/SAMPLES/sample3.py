# sample3.py
# simple API facade combining two utilities

class AuthService:
    def login(self, user, pw):
        print(f'logging in {user}')
        return True

class DataService:
    def fetch(self):
        print('fetching data')
        return [1,2,3]

class API:
    def __init__(self):
        self.auth = AuthService()
        self.data = DataService()
    def get_data(self, user, pw):
        if self.auth.login(user, pw):
            return self.data.fetch()
        return []

if __name__ == '__main__':
    api = API()
    print(api.get_data('alice','secret'))
