# sample3.py
# Mediator coordinating workflow between components

class WorkflowMediator:
    def __init__(self):
        self.steps = []

    def register_step(self, step):
        step.mediator = self
        self.steps.append(step)

    def advance(self, current_step):
        if current_step in self.steps:
            idx = self.steps.index(current_step)
            if idx + 1 < len(self.steps):
                return self.steps[idx + 1]
        return None


class Step:
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def execute(self):
        print(f"Executing {self.name}")
        next_step = self.mediator.advance(self)
        return next_step


def main():
    mediator = WorkflowMediator()
    step1 = Step("Step 1")
    step2 = Step("Step 2")
    step3 = Step("Step 3")

    mediator.register_step(step1)
    mediator.register_step(step2)
    mediator.register_step(step3)

    current = step1
    while current:
        current = current.execute()


if __name__ == "__main__":
    main()
