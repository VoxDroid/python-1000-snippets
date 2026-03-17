# sample3.py
# Event dispatcher with event types

from collections import defaultdict


class EventDispatcher:
    def __init__(self):
        self._listeners = defaultdict(list)

    def register(self, event_type, listener):
        self._listeners[event_type].append(listener)

    def dispatch(self, event_type, data=None):
        for listener in self._listeners[event_type]:
            listener(data)


def main():
    dispatcher = EventDispatcher()

    dispatcher.register("start", lambda data: print("started", data))
    dispatcher.register("stop", lambda data: print("stopped", data))

    dispatcher.dispatch("start", {"time": 1})
    dispatcher.dispatch("stop", {"time": 2})


if __name__ == "__main__":
    main()
