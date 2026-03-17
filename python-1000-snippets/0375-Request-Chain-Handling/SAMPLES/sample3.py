# sample3.py
# Chain of responsibility for event processing with logging

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, event):
        if self.successor:
            return self.successor.handle(event)
        return "No handler"


class LoggingHandler(Handler):
    def handle(self, event):
        print("Logging event:", event)
        return super().handle(event)


class ErrorHandler(Handler):
    def handle(self, event):
        if event.get("type") == "error":
            return "Error handled"
        return super().handle(event)


def main():
    chain = LoggingHandler(ErrorHandler())
    print(chain.handle({"type": "info"}))
    print(chain.handle({"type": "error"}))


if __name__ == "__main__":
    main()
