# sample1.py
# Chain of responsibility for request validation

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if self.successor:
            return self.successor.handle(request)
        return "Unhandled"


class AuthHandler(Handler):
    def handle(self, request):
        if request.get("user") == "admin":
            return "Authenticated"
        return super().handle(request)


class DataHandler(Handler):
    def handle(self, request):
        if request.get("data"):
            return f"Processed {request['data']}"
        return super().handle(request)


def main():
    chain = AuthHandler(DataHandler())
    print(chain.handle({"user": "admin", "data": "x"}))
    print(chain.handle({"user": "guest", "data": "x"}))


if __name__ == "__main__":
    main()
