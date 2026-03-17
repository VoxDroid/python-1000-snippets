# sample1.py
# Simple lock FSM with explicit state transitions

class Lock:
    def __init__(self):
        self.state = "locked"

    def enter(self, action):
        if self.state == "locked" and action == "unlock":
            self.state = "unlocked"
        elif self.state == "unlocked" and action == "lock":
            self.state = "locked"
        return self.state


def main():
    lock = Lock()
    print(lock.enter("unlock"))
    print(lock.enter("lock"))


if __name__ == "__main__":
    main()
