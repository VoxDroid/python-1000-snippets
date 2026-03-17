# sample3.py
# FSM with callback-based transitions

class StateMachine:
    def __init__(self, initial_state):
        self.state = initial_state
        self.handlers = {}

    def add_transition(self, state, event, handler):
        self.handlers[(state, event)] = handler

    def on_event(self, event, *args, **kwargs):
        key = (self.state, event)
        handler = self.handlers.get(key)
        if handler:
            self.state = handler(*args, **kwargs)
        return self.state


def main():
    sm = StateMachine("idle")

    def start():
        return "running"

    def stop():
        return "idle"

    sm.add_transition("idle", "start", start)
    sm.add_transition("running", "stop", stop)

    print(sm.on_event("start"))
    print(sm.on_event("stop"))


if __name__ == "__main__":
    main()
