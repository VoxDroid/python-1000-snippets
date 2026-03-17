# sample3.py
# Memento storing multiple fields as a dictionary

class Memento:
    def __init__(self, state):
        self.state = dict(state)


class Originator:
    def __init__(self):
        self.state = {}

    def set_state(self, **kwargs):
        self.state.update(kwargs)

    def save(self):
        return Memento(self.state)

    def restore(self, memento):
        self.state = dict(memento.state)


def main():
    o = Originator()
    o.set_state(x=1)
    m1 = o.save()

    o.set_state(y=2)
    m2 = o.save()

    o.set_state(z=3)
    o.restore(m1)
    print(o.state)


if __name__ == "__main__":
    main()
