# sample1.py
# numeric priority chain from README

class Handler:
    def __init__(self, successor=None):
        self._successor = successor
    def handle(self, request):
        pass

class LowPriorityHandler(Handler):
    def handle(self, request):
        if request <= 10:
            return f"Handled by Low: {request}"
        return self._successor.handle(request) if self._successor else "Not handled"

class HighPriorityHandler(Handler):
    def handle(self, request):
        if request > 10:
            return f"Handled by High: {request}"
        return self._successor.handle(request) if self._successor else "Not handled"

if __name__ == '__main__':
    chain = LowPriorityHandler(HighPriorityHandler())
    print(chain.handle(5))
    print(chain.handle(15))
