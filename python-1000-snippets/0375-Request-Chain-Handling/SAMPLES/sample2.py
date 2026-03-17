# sample2.py
# Chain of responsibility for request routing

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if self.successor:
            return self.successor.handle(request)
        return "No handler"


class GetHandler(Handler):
    def handle(self, request):
        if request.get("method") == "GET":
            return "Handled GET"
        return super().handle(request)


class PostHandler(Handler):
    def handle(self, request):
        if request.get("method") == "POST":
            return "Handled POST"
        return super().handle(request)


def main():
    chain = GetHandler(PostHandler())
    print(chain.handle({"method": "GET"}))
    print(chain.handle({"method": "POST"}))
    print(chain.handle({"method": "PUT"}))


if __name__ == "__main__":
    main()
