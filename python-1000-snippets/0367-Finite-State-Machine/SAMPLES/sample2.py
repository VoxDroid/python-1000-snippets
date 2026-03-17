# sample2.py
# FSM using a transition table for clarity

class FSM:
    def __init__(self, transitions, start_state):
        self.transitions = transitions
        self.state = start_state

    def on_event(self, event):
        key = (self.state, event)
        if key in self.transitions:
            self.state = self.transitions[key]
        return self.state


def main():
    transitions = {
        ("locked", "coin"): "unlocked",
        ("unlocked", "push"): "locked",
    }
    fsm = FSM(transitions, "locked")
    print(fsm.on_event("coin"))
    print(fsm.on_event("push"))


if __name__ == "__main__":
    main()
